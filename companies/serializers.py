from rest_framework import serializers, response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
import logging
from .models import Company
logger = logging.getLogger("logger")


class CompanyModelSerializer(serializers.ModelSerializer):
    symbol = serializers.CharField()
    class Meta:
        model = Company
        fields = ("name", "description", "symbol", "market_values")


    def validate_name(self, value):
        if not len(value) <= 5:
            raise serializers.ValidationError("The name can't be greater than 50 characters")
        return value
    
    def validate_description(self, value):
        if not len(value) <= 100:
            raise serializers.ValidationError("The Description can't be greater than 100 characters")
        return value
    
    def validate_symbol(self, value):
        if not len(value) <= 10:
            raise serializers.ValidationError("The Symbol can't be greater than 10 characters")
        return value
    
    def validate_market_values(self, value):
        if not len(value) <= 50:
            raise serializers.ValidationError("The Market values can't be greater than 50 characters")
        return value


   
    def create(self, validate_data):
        try:
            obj = Company.objects.create(**validate_data)
            return obj
        except Exception as e:
            logger.error("companies.serializers.create {}".format(str(e)))

    def update(self, instance, validated_data):
        try:
            return super().update(instance, validated_data)
        except Exception as e:
            logger.error("companies.serializers.update {}".format(str(e)))
    
