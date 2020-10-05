import jwt
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from authentication.constants import UserAccountActionEnum, AUTH_TOKEN_EXPIRATION_TIME
from authentication.utils import get_current_time, id_generator
from authentication.validators import validate_phone_number
from .constants import CHAR_LEM_NORM, OT_TOKEN_EXPIRATION_TIME
from django.db import models, IntegrityError


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        user = self.model(**extra_fields)
        user.set_password(extra_fields.get('password'))
        user.save(using=self._db)
        return user

    def create_user(self, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(**extra_fields)

    def create_superuser(self, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(**extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Email and password are required. Other fields are optional.
    """
    public_id = models.IntegerField(default=id_generator, unique=True)
    username = models.CharField(
        _('username'),
        max_length=CHAR_LEM_NORM, blank=False, null=True,
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        _('email address'),
        blank=False,
        unique=True,
        error_messages={
            'unique': _("A user with that email address already exists."),
        },
    )
    full_name = models.CharField(_('full name'), max_length=CHAR_LEM_NORM, blank=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_email_confirmed = models.BooleanField(
        _('email confirmed'),
        default=False,
        help_text=_(
            'Designates whether this user has confirmed their email. '
        ),
    )
    date_joined = models.DateTimeField(
        _('date joined'),
        default=get_current_time
    )
    is_live = models.BooleanField(
        default=False
    )
    ot_token = models.IntegerField(
        default=id_generator,
        unique=True
    )
    ot_token_date = models.DateTimeField(
        _('last reset password token update date'),
        default=get_current_time
    )
    phone_number = models.CharField(
        validators=[validate_phone_number],
        max_length=28,
        null=True,
        blank=True
    )
    objects = UserManager()
    USERNAME_FIELD = 'email'


    def serialize(self, extra_info=True):
        data =  {
            'public_id': self.public_id,
            'email': self.email,
            'username': self.username,
            'full_name': self.full_name,
            'phone_number': self.phone_number
        }
        if extra_info:
            data['token'] = self.token
        return data


    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return self.full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.email

    def get_ot_token(self):
        exp_day, exp_hour, exp_min, exp_sec = OT_TOKEN_EXPIRATION_TIME
        if timezone.datetime.utcnow() > self.ot_token_date + timezone.timedelta(days=exp_day,
                                                                                hours=exp_hour,
                                                                                minutes=exp_min,
                                                                                seconds=exp_sec):
            self._generate_ot_token()
        return self.ot_token

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def _generate_ot_token(self):
        self.ot_token = id_generator()
        self.ot_token_date = get_current_time()
        try:
            self.save()
        except IntegrityError:
            self._generate_ot_token()
        return self.ot_token

    def regenerate_jwt(self):
        self._generate_jwt_token()


    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        exp_day, exp_hour, exp_min, exp_sec = AUTH_TOKEN_EXPIRATION_TIME

        token = jwt.encode({
            'id': self.pk,
            'expiration_time': str(get_current_time() + timezone.timedelta(days=exp_day,
                                                                           hours=exp_hour,
                                                                           minutes=exp_min,
                                                                           seconds=exp_sec))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')


class UserAccountAction(models.Model):
    username = models.CharField(max_length=150, null=True)
    timestamp = models.DateTimeField(default=get_current_time)
    user_action = models.IntegerField(choices=UserAccountActionEnum.members(), null=True)
    additional_params = models.TextField(null=True)

    @classmethod
    def record(cls, user_action, username=None, params=None):
        cls(username=username,
            user_action=user_action.value,
            additional_params=params).save()


