from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from src.apps.motorcycle.tests.factories import (
    MotorcycleBrandFactory,
    MotorcycleFactory,
)


class MotorcycleAPITestCase(APITestCase):
    def _setup_fixtures(self):
        self.brand = MotorcycleBrandFactory()
        self.motorcycle = MotorcycleFactory(brand=self.brand)

    def setUp(self):
        self._setup_fixtures()

        self.url_list = reverse("motorcycle:models-list", args=(self.brand.pk,))
        self.url_detail = reverse(
            "motorcycle:models-detail", args=(self.brand.pk, self.motorcycle.pk)
        )

    def test_list_motorcycles(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_motorcycle(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
