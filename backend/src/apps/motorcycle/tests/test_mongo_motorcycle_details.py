from bson import ObjectId
from rest_framework.test import APITestCase

from src.apps.motorcycle.mongo_models import MotorcycleDetails
from src.mongodb.utils import MongoTestTearDown


class MotorcycleDetailsTestCase(MongoTestTearDown, APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data = {"motorcycle_id": 1, "model": "Leoncino", "year": 2000}
        cls.model = MotorcycleDetails

        cls.instance_id = "65d8c068376dcb02571d7947"
        cls.detail_raw_data = {
            "motorcycle_id": 1,
            "model": "Leoncino Trail",
            "year": 2018,
        }
        cls.detail_data = {"_id": ObjectId(cls.instance_id), **cls.detail_raw_data}

    def test_init_instance(self):
        instance = self.model(**self.detail_data)
        self.assertEqual(
            instance.dict(), {"id": self.instance_id, **self.detail_raw_data}
        )

    def test_save_instance(self):
        instance = self.model(**self.detail_raw_data)
        self.assertIsNone(instance.id)
        instance.save()
        self.assertIsNotNone(instance.id)

        result = self.model.get_collection().find_one(ObjectId(instance.id))
        self.assertIsNotNone(result)
        self.assertEqual(str(result["_id"]), instance.id)
