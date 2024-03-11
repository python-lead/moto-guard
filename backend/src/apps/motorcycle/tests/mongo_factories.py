import factory

from src.apps.motorcycle.mongo_models import MotorcycleDetails


class MotorcycleDetailsFactory(factory.mogo.MogoFactory):
    class Meta:
        model = MotorcycleDetails

    motorcycle_id = factory.Sequence(lambda n: n + 1)
    model = factory.Faker("word")
    year = factory.Faker("random_int", min=2000, max=2023)
