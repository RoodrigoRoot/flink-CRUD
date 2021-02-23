"""
This file is to serializer Company Model and
Create validations to create, or update a Object Company
"""

from rest_framework import serializers, response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
import logging
import requests
from .models import Company

logger = logging.getLogger("logger")
API_KEY = "c0qavjf48v6s0mp617v0" # Api key to get data from api (https://finnhub.io)

class CompanyModelSerializer(serializers.ModelSerializer):
    """
    Serializer to Company Model.
    Only set attributes to ModelSerializer
    """
    symbol = serializers.CharField()
    class Meta:
        model = Company
        fields = ("auto_id","name", "description", "symbol", "market_values")

    def validate_name(self, value):
        """
        This method is to validate that the name is less than
        or equals to 50 charecters
        """
        if not len(value) <= 50:
            raise serializers.ValidationError("The name can't be greater than 50 characters")
        return value
    
    def validate_description(self, value):
        """
        This method is to validate that the name is less than
        or equals to 100 charecters
        """
        if not len(value) <= 100:
            raise serializers.ValidationError("The Description can't be greater than 100 characters")
        return value
    
    def validate_symbol(self, value):
        """
        This method has three validations
        1.-That symbol can-t be greater than 100 characteres
        2.-The symbol is ok only is accepted in
           companies registered on the New York Stock Exchange.
        3.-If the symbol exists in our DB, you can't longer register again
        """
        if not len(value) <= 10:
            raise serializers.ValidationError("The Symbol can't be greater than 10 characters")
        
        if Company.objects.filter(symbol=value).exists():
            raise serializers.ValidationError("The Symbol are you already registered. Try another Symbol")
        
        response = requests.get("https://finnhub.io/api/v1/search?q={}&token=c0qavjf48v6s0mp617v0".format(value)) # We consume Api to check if symbol exists in new york stock exchange

        if not response.json()["count"]:
            raise serializers.ValidationError("it's not exists this symbol in companies registered on the New York Stock Exchange.")

        return value
        
    def validate_market_values(self, value):
        """
        Method, to validate market values.
        Market values are Array with 50 elements
        """
        if not len(value) <= 50:
            raise serializers.ValidationError("The Market values can't be greater than 50 elements")
        return value
   
    def create(self, validate_data):
        """
        Override method Create to add logger if an error ocurrs.
        """
        try:
            obj = Company.objects.create(**validate_data)
            return obj
        except Exception as e:
            logger.error("companies.serializers.create {}".format(str(e)))

    def update(self, instance, validated_data):
        """
        Override method update to add logger if an error ocurrs.
        """
        try:
            return super().update(instance, validated_data)
        except Exception as e:
            logger.error("companies.serializers.update {}".format(str(e)))
    
