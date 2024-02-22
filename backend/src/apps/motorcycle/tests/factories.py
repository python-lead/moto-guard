import factory

from src.apps.motorcycle.models import Motorcycle, MotorcycleBrand


class MotorcycleBrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MotorcycleBrand

    name = factory.Faker("company")
    country_of_origin = factory.Faker("country")
    year_established = factory.Faker("year")


class MotorcycleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Motorcycle

    brand = factory.SubFactory(MotorcycleBrandFactory)
    displacement = factory.Faker("random_int", min=100, max=2000)
    drive_type = factory.Faker(
        "random_element", elements=Motorcycle.DriveTypeChoices.choices
    )
    model = factory.Faker("word")
    short_description = factory.Faker("sentence")
    type = factory.Faker(
        "random_element",
        elements=Motorcycle.Type.choices,
    )
    year = factory.Faker("random_int", min=1980, max=2024)
