from django.urls import path

from administration.views import items,orders,users

urlpatterns = [
    path('dashboard/',items.DashboardView.as_view(),name='dashboard'),
    path('Items/',items.ItemsView.as_view(),name='listitems'),
    path('Item/',items.ItemView.as_view(),name='detailsitem'),
    path('CreateItem/',items.CreateItemView.as_view(),name='createitem'),
    path('deleteitem/',items.DeleteItemView.as_view(),name='deletitem'),

    path('Orders/',orders.OrdersView.as_view(),name='listorders'),
    path('Order/',orders.OrderView.as_view(),name='detailsorder'),

    path('Users/',users.UsersView.as_view(),name='listusers'),

    
    ]
