import uuid

from django.utils import timezone


def get_current_time():
    return timezone.datetime.utcnow()


def id_generator():
    return uuid.uuid4().int % 1000000000