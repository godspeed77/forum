'''from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")
'''

from django.shortcuts import render
from block.models import Block
from django.contrib.auth.models import User
from django.http import HttpResponse
import uuid
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from activate.models import Activatecode

'''
def index(request):
    return render(request,'cssindex.html')

def index(request):
    block_infos =[{"name":"运维专区", "desc":"讨论区", "manager":"liquan"},
                  {"name":"django专区", "desc":"讨论区", "manager":"admin"},
                  {"name":"部落建设", "desc":"事宜", "manager":"admin"}]
    return render(request,"cssindex.html",{"blocks":block_infos})
'''

def index(request):
    block_infos = Block.objects.filter(status=0).order_by("-id")
    return render(request,"cssindex.html",{"blocks":block_infos})

def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    else:
        username = request.POST["username"].strip()
        email = request.POST["email"].strip()
        password1 = request.POST["password1"].strip()
        password2 = request.POST["password2"].strip()
        alluser = User.objects.filter(is_staff=True).order_by("-id")
        allusername = [i.username for i in alluser]
        if password1 != password2:
            return render(request,"register.html",{"error1":"两次密码不同"})
        elif username in allusername:
            return render(request,"register.html",{"error2":"用户已存在"})
        else:
            user = User(username=username,password=password1,email=email)
            user.is_active=False
            user.is_staff=True
            user.is_superuser=True
            user.save()
            new_code = str(uuid.uuid4()).replace("-","")
            now = timezone.now()
            oneday = timedelta(days=1)
            expire_timestamp = now + oneday
            actcode = Activatecode(user=username, new_code=new_code, expire_timestamp=expire_timestamp)
            actcode.save()
            active_link = "http://%s/activate/%s" % (request.get_host(),new_code)
            active_mail = '''点击<a href="%s">这里</a>激活 ''' % active_link
            send_mail(subject='[Python部落]激活邮件',
                     message='点击链接激活: %s' % active_link,
                     html_message=active_mail,
                     from_email='monitor0530@126.com',
                     recipient_list=[email],
                     fail_silently=False)
            
            return HttpResponse("请前往您的邮箱激活账号")
