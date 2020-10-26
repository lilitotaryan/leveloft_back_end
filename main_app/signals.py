from main_app.utils import uuid_hash
from .models import Address
from django.db import models
from django.dispatch import receiver
from django.db.utils import IntegrityError

@receiver(models.signals.pre_save, sender=Address)
def generate_hash_address(sender, instance, **kwargs):
    address_hash = uuid_hash(address1 = instance.address1,
                             city = instance.city,
                             state = instance.state,
                             country = instance.country)
    if not instance.hash == address_hash:
        try:
            instance.hash = address_hash
        except IntegrityError:
            return False
