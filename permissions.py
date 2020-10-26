from rest_framework.permissions import BasePermission
from django.conf import settings
import secrets

from api_exceptions import NotAuthorizedError


class RequiredAPIToken(BasePermission):

    def has_permission(self, request, view):
        try:
            x_api_key = request.META['HTTP_X_API_KEY']
        except Exception:
            raise NotAuthorizedError
        if secrets.compare_digest(settings.HTTP_X_API_KEY, x_api_key):
            return True
        else:
            raise NotAuthorizedError