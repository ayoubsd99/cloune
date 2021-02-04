from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from core.models import BaseModel

from core.views import _gref


class Profile(BaseModel):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    
    def __str__(self):
        return self.reference
    def generate(self):
        while True :
            random = _gref(25)
            if Profile.objects.filter(reference=random).exists():
                continue
            self.reference = random
            break
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(Profile, self).save(*args, **kwargs) # Call the real save() method

class User(AbstractUser, BaseModel) :
    permission = models.ForeignKey("core.AppPermission", on_delete=models.CASCADE)
    profile = models.OneToOneField("users.Profile", on_delete=models.CASCADE)

    def __str__(self):
        return self.reference

    def generate(self):
        while True :
            random = _gref(25)
            if User.objects.filter(reference=random).exists():
                continue
            self.reference = random
            break
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(User, self).save(*args, **kwargs) # Call the real save() method
class Admin(User):

    def __str__(self):
        return self.reference

        
    