from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

# Create your models here.

class Company(models.Model):
    
    auto_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=50)
    description = models.CharField(verbose_name="Description", max_length=100)
    symbol = models.CharField(verbose_name="Symbol", max_length=10)
    market_values = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
