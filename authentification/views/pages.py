from django.shortcuts import render,HttpResponseRedirect
from django.utils.html import escapejs
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

from django.views import View

APPLICATION='authentification'
class SigninView(View):
    view_name='signin'
    template=f'{APPLICATION}/{view_name}'
    def get(self, request, *args, **kwargs):
        if user.request.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard', ))
            
        return render(request, self.template)
        

    def post(self, request, *args, **kwargs):
        username=escapejs(request.POST.get('username',None))
        password=escapejs(request.POST.get('password',None))
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('dashboard', ))
            
        return HttpResponseRedirect(reverse('signin', ))
        

class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('signin', ))
               