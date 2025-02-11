from django.urls import path, include
from . import views

# urlpatterns = [
#     path('buildings', views.BuildingList.as_view()),
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'buildings', views.BuildingModelView)
router.register(r'floors', views.FloorModelView)
router.register(r'apartments', views.ApartmentModelView)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]