from django.db import models
from django.utils.text import capfirst

class BaseModel(models.Model):

    def get_plural_model_name(self):
        return self._meta.verbose_name_plural

    class Meta:
        abstract = True
