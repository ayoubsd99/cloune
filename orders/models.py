from django.db import models

# Create your models here.
from core.models import BaseModel
from core.views import _gref,check_email,check_phone


class Customer(BaseModel):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_gref(25)
            if Customer.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(Customer, self).save(*args, **kwargs) # Call the real save() method       
      
class Order(BaseModel):
    customer=models.ForeignKey("orders.Customer",on_delete=models.CASCADE)
    payment=models.ForeignKey("orders.Payment",on_delete=models.CASCADE)

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_gref(25)
            if Order.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(Order, self).save(*args, **kwargs) # Call the real save() method       
      
class Line(BaseModel):
    item=models.ForeignKey("items.Item",on_delete=models.CASCADE)
    qty=models.IntegerField()
    total = models.FloatField()
    order=models.ForeignKey("orders.Order", on_delete=models.CASCADE)

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_gref(25)
            if Line.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(Line, self).save(*args, **kwargs) # Call the real save() method       
      
class PaymentStatus(BaseModel):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_gref(25)
            if PaymentStatus.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(PaymentStatus, self).save(*args, **kwargs) # Call the real save() method       

class Payment(BaseModel):
    amount = models.FloatField()
    status=models.ForeignKey("orders.PaymentStatus", on_delete=models.CASCADE)   

    def __str__(self):
        return self.reference


    def generate(self):
        while True:
            random=_gref(25)
            if Payment.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(Payment, self).save(*args, **kwargs) # Call the real save() method       
