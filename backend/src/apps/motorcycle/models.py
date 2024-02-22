from django.db import models


class MotorcycleBrand(models.Model):
    name = models.CharField(max_length=256)
    country_of_origin = models.CharField(max_length=256, null=True)
    year_established = models.PositiveIntegerField(null=True, blank=True)


class Motorcycle(models.Model):
    class Type(models.TextChoices):
        ADVENTURE = "Adventure", "Adventure"
        CRUISER = "Cruiser", "Cruiser"
        DUAL_SPORT = "Dual Sport", "Dual Sport"
        ELECTRIC = "Electric", "Electric"
        NAKED = "Naked", "Naked"
        OFF_ROAD = "Off-Road", "Off-Road"
        OTHER = "OTHER", "Other"
        SCOOTER = "Scooter", "Scooter"
        SPORT = "Sport", "Sport"
        STANDARD = "Standard", "Standard"
        TOURING = "Touring", "Touring"

    class DriveTypeChoices(models.TextChoices):
        BELT = "Belt", "Belt"
        CHAIN = "Chain", "Chain"
        SHAFT = "Shaft", "Shaft"

    brand = models.ForeignKey(MotorcycleBrand, on_delete=models.CASCADE)
    displacement = models.PositiveIntegerField()
    drive_type = models.CharField(max_length=256, choices=DriveTypeChoices.choices)
    model = models.CharField(max_length=256)
    short_description = models.CharField(max_length=256, null=True, blank=True)
    type = models.CharField(max_length=256, choices=Type.choices)
    year = models.PositiveIntegerField()
