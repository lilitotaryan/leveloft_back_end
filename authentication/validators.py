import phonenumbers as phonenumbers
from django.core.exceptions import ValidationError
from phonenumbers import NumberParseException


def validate_phone_number(number: str):
    try:
        parsed = phonenumbers.parse(number, None)
    except NumberParseException:
        raise ValidationError(
            _("%(value)s is not a valid phone number. Please use +12345678901 format."),
            params={'value': number}
        )

    if not phonenumbers.is_possible_number(parsed):
        raise ValidationError(
            _("%(value)s is not a valid phone number. Please use +12345678901 format."),
            params={'value': number}
        )