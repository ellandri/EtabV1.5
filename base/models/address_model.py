from django.db import models

from base.models.helpers.date_time_model import DateTimeModel


class AddressModel(DateTimeModel):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self) :
      return f"{self.city} {self.street} {self.country} "

