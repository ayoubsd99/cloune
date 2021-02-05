from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.urls import reverse
from django.utils.html import escapejs
from django.views import View
from django.contrib import messages

import cloudinary

from items.models import Item,GroupOption,ItemImage,Option,Category,Variant

APPLICATION='administration'

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        view_name='dashboard'
        template=f'{APPLICATION}/{view_name}.html'
        if not user.request.is_authenticated:
            return HttpResponseRedirect(reverse('signin', ))
            
        return render(request, self.template)
        
class ItemsView(View):
    view_name='items'
    template=f'{APPLICATION}/{view_name}.html'
    def get(self, request, *args, **kwargs):
        context={
            'items':Item.objects.all()
        }
        return render(request, self.template,context)
    def post(self,request):
        
        return HttpResponseRedirect(reverse('listitems', ))

class ItemView(View):
    view_name='item'
    template=f'{APPLICATION}/{view_name}.html'
    def get(self, request, *args, **kwargs):
        item_reference=kwargs.get('item_reference')
        context={
            'item':get_object_or_404(Item,reference=item_reference)
        }
        return render(request, self.template,context)
        
class CreateItemView(View):
    view_name='createitem'
    def get(self, request, *args, **kwargs):
        template=f'{APPLICATION}/{view_name}.html'
        return render(request, self.template)
        
    def post(self,request):
        title=escapejs(request.POST.get("title",None))
        small_desc=escapejs(request.POST.get("small_desc",None))
        big_desc=escapejs(request.POST.get("big_desc",None))
        option1=escapejs(request.POST.get("option1",None))
        option2=escapejs(request.POST.get("option2",None))
        option3=escapejs(request.POST.get("option3",None))
        category=escapejs(request.POST.get("category",None))
        price=escapejs(request.POST.get("price",None))
        discount_price=escapejs(request.POST.get("discount_price",None))
        image1=request.FILES("image1")
        image1=request.FILES("image2")
        image1=request.FILES("image3")
        if(option1 is None or option2 is None or option3 is None or
        category is None or price is None or discount_price is None or
        title is None or small_desc is None or big_desc is None):

            return HttpResponseRedirect(reverse('CreateItem', ))
        try:
            cat=get_object_or_404(Category,name=category)        
            opti1=Option.objects.create(label=option1)
            opti2=Option.objects.create(label=option2)
            opti3=Option.objects.create(label=option3)
            grp_op=GroupOption.objects.create(opti1,opti2,opti3)
            variant=Variant.objects.create(price=float(price),discount_price=float(discount_price),group_option=grp_op)
            item=Item.objects.create(title=title,small_desc=small_desc,big_desc=big_desc,category=cat,varient=variant)
            images=[image1,image2,image3]
            urls=[]
            for image in images:
                urls.append(response['secure_url'])
            for url in urls:
                ItemImage.objects.create(item=item,image=url)    
            messages.success(request,'data added succesfuly')  
        except:
            messages.error(request,'failed to add data')
            return HttpResponseRedirect(reverse('CreateItem', ))
        
        return HttpResponseRedirect(reverse('listitems', ))
        
class DeleteItemView(View):
    def get(self, request, *args, **kwargs):
        item_reference=kwargs.get('item_reference',None)
        if item_reference is None:
            messages.warning('item donse not exisis')
        item=get_object_or_404(Item,reference=item_reference)
        item.deleted=not item.deleted
        item.save()
        return HttpResponseRedirect(reverse('itemdetails', ))
            
