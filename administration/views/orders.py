from django.shortcuts import render, get_object_or_404

from django.views import View

from orders.models import Order

APPLICATION='administration'
class OrdersView(View):
    view_name='orders'
    template=f'{APPLICATION}/{view_name}.html'
    def get(self, request, *args, **kwargs):
        context={
            'orders':Order.objects.all()
        }
        return render(request, self.template,context)
        
class OrderView(View):
    view_name='order'
    template=f'{APPLICATION}/{view_name}.html'
    def get(self, request, *args, **kwargs):
        order_reference=kwargs.get('order_reference')
        context={
            'order':get_object_or_404(Order,reference=order_reference)
        }
        return render(request, self.template,context)
        
