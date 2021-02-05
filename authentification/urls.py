from django.urls import path

from authentification.views.pages import SigninView,LogoutView
 
urlpatterns = [
   path('signin/',SigninView.as_view(),name='signin'),
   path('logout/',LogoutView.as_view(),name='logout'),

    
]