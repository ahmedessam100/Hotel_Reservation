from django.db import models
from Customer.models import customer
from Room.models import room

class Reservations(models.Model):
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    room_id =  models.ForeignKey(room, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    from_date = models.DateTimeField('Date')
    to_date = models.DateTimeField('Date')
