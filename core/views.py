from django.shortcuts import render

# Create your views here.
import string
import random
import re 

def _gref(length):
    letters=string.hexdigits
    return ''.join(random.choice(letters)for i in range(length))

def check_email(email):
    return re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email) 


def check_phone(phone):
    return   re.search('\w{3}-\w{3}-\w{4}',email)    