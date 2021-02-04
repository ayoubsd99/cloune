from django.shortcuts import render,get_object_or_404
from django.views import View


from users.models import User


APPLICTAION='administration'
class UsersView(View):
    view_name='users'
    template=f'{APPLICTAION}/{view_name}.html'
    def get(self, request, *args, **kwargs):
        context={
            'users':User.objects.all()
        }
        return render(request, sefl.template,context)
        
        