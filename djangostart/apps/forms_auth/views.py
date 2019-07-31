from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm

def index(request,template_name):
    return render(request,template_name)

#登录函数，使用auth
def _login(request,username,password):
    ret = True
    # authenticate: 认证成功=> 返回用户, 认证失败=>None
    user  = authenticate(username=username,password=password)
    if user:
        #用户可用状态
        if user.is_active:
            #登录
            auth_login(request,user)
        else:
            print("用户不可用")
            messages.add_message(request,messages.INFO,"用户不可用")
            ret =  False
    else:
        print("用户认证失败")
        messages.add_message(request,messages.INFO,"用户认证失败")
        ret = False
    return ret

def login(request):
    # 提交:POST
    # 直接访问:GET
    print(request.method)
    # form表单实例化:空的表单
    form = LoginForm()
    if request.method == "POST":
        # check data
        # 表单数据绑定
        form = LoginForm(request.POST)
        # is_valid: 验证表单数据是否合法(合法返回True)
        if form.is_valid():
            ret = _login(request, form.cleaned_data["username"], form.cleaned_data["password"])
            if ret :
                return redirect(reverse("forms_auth:index"))
    return  render(request,"forms_auth/login.html",{"form":form})

def register(request):
    form = RegisterForm()
    if request.method =="POST":
        # 将数据绑定到RegisterForm表单
        form = RegisterForm(request.POST)
        # is_valid: 验证表单数据是否合法(合法返回True)
        # 用户名唯一、邮箱唯一、两个密码一致
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            # 　方法一：
            # user = User.objects.filter(username=username)
            # if password1 == password2 and not user:
            #     user = User.objects.create_user(username, email, password1)
            #     user.save()
            #     _login(request, username, password1)
            #     # 注册完毕 直接登陆
            #     return redirect(reverse("forms_auth:index"))

            # 方法二、利用Form的clean进行验证
            user  = User.objects.create_user(username,email,password1)
            user.save()

            #注册完毕，直接登录
            _login(request,username,password1)

            return redirect(reverse("forms_auth:index"))
    return render(request, "forms_auth/register.html", {"form":form})

def logout(request):
    auth_logout(request)
    return redirect(reverse('forms_auth:login'))


