from django.urls import path

from landing.views.items import Items_data,CatalogView,ItemView

from landing.views.orders import create_order,CreateOrderView
 
urlpatterns = [
    path('api/items',Items_data),
    path('cataloge/',CatalogView.as_view(),name='catalogue'),
    path('detailsitem/',ItemView.as_view(),name='detailsitem'),

    path('api/createorder',create_order),
    path('createorder/',CreateOrderView.as_view(),name='createorder'),



    
]
