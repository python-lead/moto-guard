from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from src.apps.motorcycle.tests.factories import MotorcycleBrandFactory


class MotorcycleBrandAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url_list = reverse("motorcycle:brands-list")

    def setUp(self):
        self.motorcycle_brand = MotorcycleBrandFactory()

        self.url_detail = reverse(
            "motorcycle:brands-detail", args=(self.motorcycle_brand.pk,)
        )

    def test_list_motorcycles(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_motorcycle(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
