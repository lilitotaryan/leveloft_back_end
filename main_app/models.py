from django.db import models
from django.core.exceptions import ValidationError
from base_model import BaseModel
from main_app.constants import STRING_LEN_MAX, CHAR_LEN_MIN
from main_app.utils import id_generator, uuid_hash, upload_directory_path
from django.utils import timezone
from django.db.utils import IntegrityError


class Address(BaseModel):
    address1 = models.CharField(max_length=CHAR_LEN_MIN, blank=False, default=None)
    city = models.CharField(max_length=CHAR_LEN_MIN, blank=False, default=None)
    state = models.CharField(max_length=CHAR_LEN_MIN, blank=False, default=None)
    country = models.CharField(max_length=CHAR_LEN_MIN, blank=False, default=None)
    zip_code = models.CharField(max_length=CHAR_LEN_MIN, blank=True, default=None)
    hash = models.UUIDField(unique=True, blank=True, default=None)

    def clean(self):
        address_hash = uuid_hash(address1=self.address1,
                                 city=self.city,
                                 state=self.state,
                                 country=self.country)
        if not self.hash == address_hash:
            if Address.objects.filter(hash=address_hash):
                raise ValidationError('The Address already exists.')

    def __str__(self):
        return f'{self.country} {self.city} {self.state} {self.address1}'

class Building(BaseModel):
    public_id = models.IntegerField(default=id_generator, unique=True)
    description = models.CharField(max_length=STRING_LEN_MAX, blank=True)
    name = models.CharField(max_length=CHAR_LEN_MIN, blank=False)
    image = models.FileField(upload_to=upload_directory_path)
    created = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.SET_NULL)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

class Floor(BaseModel):
    public_id = models.IntegerField(default=id_generator, unique=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='floors')
    description = models.CharField(max_length=STRING_LEN_MAX, blank=True)
    image = models.FileField(upload_to=upload_directory_path)
    index = models.IntegerField()

    def __str__(self):
        return str(self.index)

class Apartment(BaseModel):
    public_id = models.IntegerField(default=id_generator, unique=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='apartments')
    number = models.CharField(blank=False, max_length=CHAR_LEN_MIN)
    is_reserved = models.BooleanField(default=False)
    image = models.FileField(upload_to=upload_directory_path)
    index = models.IntegerField()

    def __str__(self):
        return str(self.number)


