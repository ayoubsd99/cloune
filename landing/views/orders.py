from django.shortcuts import render,HttpResponseRedirect
from django.utils.html import escapejs
from django.urls import reverse
from django.contrib import messages
from orders.models import Order,Line,Customer,Payment,PaymentStatus
from core.views import check_email,check_phone

def create_order(request):
    name=escapejs(request.POST.get('name',None))
    email=escapejs(request.POST.get('email',None))
    phone=escapejs(request.POST.get('phone',None))
    address=escapejs(request.POST.get('address',None))
    city=escapejs(request.POST.get('city',None))
    country=escapejs(request.POST.get('country',None))
    amount=escapejs(request.POST.get('amount',None))
    status=escapejs(request.POST.get('status',None))
    lines=list(request.POST.get('cartitems',None))
    if (name is None,email is None,phone is None,address is None,city is None,country is None,amount is None,status is None):
        messages.warning(request,'information does not valid')
    if not check_email(email):
        messages.warning(request,'email does not valid')
    if not check_phone(phone):
        messages.warning(request,'phone number does not valid')
    try:
        customer=Customer.objects.create(name=name,phone=phone,address=address,email=email,city=city,country=country)
        paymentstatus=PaymentStatus.objects.create(name=status)
        payment=Payment.objects.create(amount=amount,status=paymentstatus)
        order=Order.objects.create(customer=customer,payment=payment)
        for line in lines:
            Line.objects.create(item=line.item,qty=line.qty,total=line.total,order=order)
            messages.success(request,'your command saved ')
    except:
        messages.error(request,'faild to add command')



