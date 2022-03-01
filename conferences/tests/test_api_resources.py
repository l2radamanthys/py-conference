from rest_framework.test import APITestCase
from conferences.models.resources import Resource


class APIResourceTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/resources")
        self.assertEqual(len(response.data["result"]), 0)
