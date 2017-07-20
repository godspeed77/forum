'''from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")
'''

from django.shortcuts import render
from block.models import Block

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
