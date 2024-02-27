from bson import ObjectId
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from src.apps.motorcycle.mongo_models import MotorcycleDetails
from src.apps.motorcycle.tests.factories import (
    MotorcycleBrandFactory,
    MotorcycleFactory,
)
from src.apps.motorcycle.tests.mongo_factories import MotorcycleDetailsFactory
from src.mongodb.utils import MongoTestTearDown


class MotorcycleDetailMongoViewSetTestCase(MongoTestTearDown, APITestCase):
    def _setup_fixtures(self):
        self.brand = MotorcycleBrandFactory()
        self.motorcycle = MotorcycleFactory(brand=self.brand)
        self.details = MotorcycleDetailsFactory(motorcycle_id=self.motorcycle.id)

    def setUp(self):
        self._setup_fixtures()

        self.detail_data = {
            "motorcycle_id": self.motorcycle.id,
            "model": "Leoncino Trail",
            "year": 2018,
        }

        self.list_url = reverse("motorcycle:mongo_moto-list")
        self.details_url = reverse(
            "motorcycle:mongo_moto-detail", args=(self.details.id,)
        )

    def test_list_details(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_details(self):
        response = self.client.get(self.details_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.details.dict())

    def test_create_details(self):
        response = self.client.post(self.list_url, data=self.detail_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        instance = MotorcycleDetails.get_collection().find_one(
            ObjectId(response.data["id"])
        )
        self.assertIsNotNone(instance)

    def test_destroy_details(self):
        response = self.client.delete(self.details_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        instance = MotorcycleDetails.get_collection().find_one(
            ObjectId(self.details.id)
        )
        self.assertIsNone(instance)

    def test_update_details(self):
        patch_data = {"model": "TRK 502 X", "year": 2020}
        response = self.client.patch(self.details_url, patch_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.details.refresh()
        self.assertEqual(self.details.model, patch_data["model"])
        self.assertEqual(self.details.year, patch_data["year"])
