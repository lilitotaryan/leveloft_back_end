from django.db import models


class Building(models.Model):
    pass

class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

class Apartment(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

class Room(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)


