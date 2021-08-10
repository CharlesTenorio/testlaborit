from rest_framework import status
from rest_framework.test import APITestCase


class LeadTestCase(APITestCase):
    def test_create_lead(self):
        data = {"name": "Charles Tenorio", "email": "charlestenorios@gmail.com"}
        response = self.client.post("/api/v1/email/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_lead(self):
        response = self.client.get("/api/v1/email/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
