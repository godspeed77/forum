from django.shortcuts import render,redirect
from .models import Activatecode
from django.contrib.auth.models import User
from django.http import HttpResponse

def activate(request,code):
    code=str(code)
    activate_user = Activatecode.objects.get(new_code=code)
    activate_username = activate_user.user
    user = User.objects.get(username=activate_username)
    user.is_active = True
    user.save()
    return HttpResponse("您的账号 %s 已激活" % activate_username)

