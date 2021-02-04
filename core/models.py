from django.db import models

# Create your models here.
from .views import _gref

class BaseModel(models.Model):
    referrence=models.CharField(max_length=50)
    created_at=models.DateField(auto_now=False, auto_now_add=True)
    updated_at=models.DateField(auto_now=True, auto_now_add=False)
    deleted=models.BooleanField(default=False)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.reference

class AppPermission(models.Model):
    label = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.label


    def generate(self):
        while True:
            random=_gref(25)
            if AppPermission.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(AppPermission, self).save(*args, **kwargs) # Call the real save() method       

class Country(BaseModel):
    label=models.CharField(max_length=50,unique=True)


    def __str__(self):
        return self.referrence

    def generate(self):
        while True:
            random=_gref(25)
            if Country.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(Country, self).save(*args, **kwargs) # Call the real save() method       

class City(BaseModel):
    label=models.CharField(max_length=50,unique=True)
    country=models.ForeignKey("core.Country",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.referrence

    def generate(self):
        while True:
            random=_gref(25)
            if City.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(City, self).save(*args, **kwargs) # Call the real save() method       
