from django.contrib.auth.models import User

from main_app.models import Building, Floor, Apartment
from main_app.renderers import ResponseRenderer
from paginators import StandardResultsSetPagination
from permissions import RequiredAPIToken
from .serializers import BuildingModelSerializer, FloorModelSerializer, ApartmentModelSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

# todo add pagination for all views
class BuildingModelView(viewsets.ModelViewSet):
    queryset = Building.objects.filter(is_valid=True).order_by('-created')
    serializer_class = BuildingModelSerializer
    lookup_field = 'public_id'
    single_object = False
    pagination_class = StandardResultsSetPagination
    renderer_classes = [ResponseRenderer]
    permission_classes = [RequiredAPIToken]

    def get_object(self):
        self.single_object=True
        return super(BuildingModelView, self).get_object()

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'single_object': self.single_object
        }


class FloorModelView(viewsets.ModelViewSet):
    queryset = Floor.objects.all().order_by('-index')
    serializer_class = FloorModelSerializer
    lookup_field = 'public_id'
    single_object = False
    renderer_classes = [ResponseRenderer]
    permission_classes = [RequiredAPIToken]

    def get_object(self):
        self.single_object=True
        return super(FloorModelView, self).get_object()

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'single_object': self.single_object
        }


class ApartmentModelView(viewsets.ModelViewSet):
    queryset = Apartment.objects.all().order_by('-index')
    serializer_class = ApartmentModelSerializer
    lookup_field = 'public_id'
    single_object = False
    renderer_classes = [ResponseRenderer]
    permission_classes = [RequiredAPIToken]

    def get_object(self):
        self.single_object=True
        return super(ApartmentModelView, self).get_object()

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'single_object': self.single_object
        }