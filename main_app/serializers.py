from rest_framework import serializers

from main_app.models import Building, Address, Floor, Apartment


class ApartmentModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        if kwargs.get('context') and kwargs.get('context').get('single_object'):
            self.Meta.fields = ('public_id', 'number', 'is_reserved', 'image', 'index')
        else:
            self.Meta.fields = ('public_id', 'is_reserved', 'index')
        super(ApartmentModelSerializer, self).__init__(*args, **kwargs)


    class Meta:
        model = Apartment
        fields = []


class FloorModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        if kwargs.get('context') and kwargs.get('context').get('single_object'):
            self.fields['apartments'] = ApartmentModelSerializer(many=True, read_only=True)
            self.Meta.fields = ('public_id', 'description', 'image', 'index', 'apartments')
        else:
            self.Meta.fields = ('public_id', 'description', 'image', 'index')
        super(FloorModelSerializer, self).__init__(*args, **kwargs)


    class Meta:
        model = Floor
        fields = []


class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address1', 'city', 'state', 'state', 'country', 'zip_code')


class BuildingModelSerializer(serializers.ModelSerializer):
    address = AddressModelSerializer(read_only=True)

    def __init__(self, *args, **kwargs):
        if kwargs.get('context') and kwargs.get('context').get('single_object'):
            self.fields['floors'] = FloorModelSerializer(many=True, read_only=True)
            self.Meta.fields = ('public_id', 'description', 'name', 'address', 'floors')
        else:
            self.Meta.fields = ('public_id', 'description', 'name', 'image', 'address')
        super(BuildingModelSerializer, self).__init__(*args, **kwargs)


    class Meta:
        model = Building
        fields = ['address']
