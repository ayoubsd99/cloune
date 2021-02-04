from django.shortcuts import get_object_or_404
from django.db import models

# Create your models here.

from core.models import BaseModel
from core.views import _gref

class Item(BaseModel):
    title=models.CharField(max_length=50)
    small_desc=models.CharField(max_length=150)
    big_desc=models.TextField()
    category=models.ForeignKey("items.Category",on_delete=models.CASCADE)
    varient=models.ForeignKey("items.Variant",on_delete=models.CASCADE)

    def get_images(self):
        images=[]
        for image in ItemImage.objects.filter(item=self):
            images.append(image)
        return images

    def get_variant(self):
        variant={}
        var= get_object_or_404(Variant,referrence=self.varient.refernce)
        variant['variant']=var
        return variant

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_gref(25)
            if Item.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(Item, self).save(*args, **kwargs) # Call the real save() method       

class ItemImage(BaseModel):
    item=models.ForeignKey("items.Item",on_delete=models.CASCADE)    
    image=models.TextField()


    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_gref(25)
            if ItemImage.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(ItemImage, self).save(*args, **kwargs) # Call the real save() method       

class Variant(BaseModel):
    price=models.BooleanField(default=0.00)
    discount_price=models.BooleanField(default=0.00)
    group_option=models.ForeignKey("items.GroupOption",on_delete=models.CASCADE)

    def __str__(self):
        return self.reference
    
    def get_options(self):
        options={}
        options['options']= get_object_or_404(GroupOption,referrence=self.group_option.reference)
        return options
        
    def generate(self):
        while True:
            random=_gref(25)
            if ItemImage.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(ItemImage, self).save(*args, **kwargs) # Call the real save() method       

class GroupOption(BaseModel):

    option1=models.ForeignKey("items.Option",related_name='option1', on_delete=models.CASCADE)   
    option2=models.ForeignKey("items.Option",related_name='option2', on_delete=models.CASCADE)    
    option2=models.ForeignKey("items.Option",related_name='option3', on_delete=models.CASCADE)    

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_gref(25)
            if GroupOption.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(GroupOption, self).save(*args, **kwargs) # Call the real save() method       

class Option(BaseModel):
    label=models.CharField(max_length=50)

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_gref(25)
            if Option.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(Option, self).save(*args, **kwargs) # Call the real save() method       

class Category(BaseModel):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_gref(25)
            if Category.objects.filter(referrence=random).exists():
                continue
            self.referrence=random
            break
        return self.referrence

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()
       super(Category, self).save(*args, **kwargs) # Call the real save() method       
      