from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase
from .models import Company
from  django.test import Client
from rest_framework import status
from django.urls import reverse
# Create your tests here.

CREATE_COMPANY_URL = reverse("create_company")


class CreateCompanyTestCase(APITestCase):


    def test_create_company(self):
        """
        Test module for Company model 
        Create object to Company
        """

        data = {# Payload

            
            "name": "apple",
            "description": "apple inc.",
            "symbol": "AAPL",
            "market_values": [
                "1,2,3,3,4"
            ]
        }

        response = self.client.post(CREATE_COMPANY_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_company(self):
        """
        Test module for Company model 
        Update object to Company
        First we create a company and then we update it
        """
        
        data = {# Payload
            "name": "apple",
            "description": "apple inc.",
            "symbol": "AAPL",
            "market_values": [
                "1,2,3,3,4"
            ]
        }

        comp = Company.objects.create(**data)
        UPDATE_COMPANY_URL = reverse("rud_company", kwargs={'auto_id':comp.auto_id})
        response = self.client.delete(UPDATE_COMPANY_URL)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_company(self):
        """
        Test module for Company model 
        Delete object to Company
        First we create a company and then we eliminate it
        """
        
        data = {# Payload
            "name": "apple",
            "description": "apple inc.",
            "symbol": "AAPL",
            "market_values": [
                "1,2,3,3,4"
            ]
        }

        comp = Company.objects.create(**data)
        UPDATE_COMPANY_URL = reverse("rud_company", kwargs={'auto_id':comp.auto_id})
        comp.name = "Changes"
        response = self.client.patch(UPDATE_COMPANY_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)