import uuid


def id_generator():
    return uuid.uuid4().int // pow(10,30)


def upload_directory_path(instance, filename):
    return f'media/{instance.get_plural_model_name()}/{filename}'

def uuid_hash(address1, city, state, country):
    return uuid.uuid3(uuid.NAMESPACE_DNS, str(address1) + str(city) + str(state) + str(country))