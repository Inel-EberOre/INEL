from django.db import models

from users.models import User
from orders.models import Order


class Charge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    charge_id = models.CharField(max_length=50)
    amount = models.IntegerField() # Centavos
    payment_method = models.CharField(max_length=50) # Id método de pago
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.charge_id