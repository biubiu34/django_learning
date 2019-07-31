from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.

def index(request):
    return HttpResponse("route_base index")

def index2(request):
    return  render(request,'route_base/index2.html')

def zoos1(request,zoo_id):
    return HttpResponse(f"zoos-{zoo_id}")
def zoos2(request,id):
    return HttpResponse(f"zoos-{id}")
def zoos3(request,id,ty):
    return HttpResponse(f"zoos-{id}-{ty}")

def login(request,static):

    if static ==1:
        #反向解析带参数
        print(reverse('route_base:zoo3',args=(10,)))
        #print(reverse("route_base:zoo3"))
        return redirect(reverse('route_base:index'))
    else:
        return HttpResponse("这是login页面")
