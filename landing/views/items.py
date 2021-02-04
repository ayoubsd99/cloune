from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from django.utils.html import escapejs

import simplejson as JSON

from items.models import Item

def single_item(item):
    return{
        'title':item.title,
        'small_desc':item.small_desc,
        'big_desc':item.big_desc,
        'images':item.get_images(),
        'variant':item.get_variant(),
        'options':item.varient.get_options()
    }

def Items_data(request):
    data={}
    json_item=[]
    
    item_reference= esca(request.POST.get("item_reference",None))
    if item_reference in None:
        try:
            item=get_object_or_404(Item,reference=item_reference)
            data['item']=single_item(item))
            data['response_code']=0
        except:
            data['response_code']=-2
            data['response_message']='item does not exists'

    items=Item.objects.all()
    for item in items:
        json_item.append(single_item(item))

    data['items']=json_item
    data['response_code']=0  
    return HttpResponse(JSON.dumps(data), content_type='application/json')
