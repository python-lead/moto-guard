from bson import ObjectId
from rest_framework.test import APITestCase

from src.apps.motorcycle.mongo_models import MotorcycleDetails
from src.apps.motorcycle.tests.mongo_factories import MotorcycleDetailsFactory
from src.mongodb.utils import MongoTestTearDown


class MotorcycleMongoFactoriesTestCase(MongoTestTearDown, APITestCase):
    def test_motorcycle_detail_factory(self):
        instance = MotorcycleDetailsFactory()

        self.assertIsNotNone(instance.id)

        result = MotorcycleDetails.get_collection().find_one(ObjectId(instance.id))
        self.assertIsNotNone(result)
        self.assertEqual(str(result["_id"]), instance.id)
