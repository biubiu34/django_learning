from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def index(request):
    #创建了一个Form表单
    form = ContactForm(request.GET)
    print(form)
    return render(request, "forms_base/index.html", {"form":form})

from django.shortcuts import render, HttpResponse,redirect,reverse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .forms import ContactForm, RegisterForm, LoginForm
from .models import UserInfo


def register(request):
    # 没有绑定数据的表单
    reg_form = RegisterForm()
    if request.method == 'POST':
        #绑定数据的表单
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            # is_valid => 用来验证表单中的所有数据中否都合法
            # 验证用户名：检查用户是否已经在数据中存在，可以对某个字段来验证
            # 给某个字段添加验证方法:定义form的时候，clean_字段名
            # 给整个表单添加验证方法：定义form的时候，加一个clean方法
            username = reg_form.cleaned_data["username"]
            password = reg_form.cleaned_data["password"]
            password = make_password(password)
            UserInfo.objects.create(username=username, password=password)
            print("合法")
            messages.add_message(request,messages.INFO,"注册成功")
            return redirect(reverse("forms_base:login"))
        else:
            print("不合法")
            messages.add_message(request, messages.INFO, "不合法")
    return render(request, 'forms_base/register.html', {"form":reg_form})


def login(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        # is_valid提交的数据合法(会检查所有字段及表单整体的合法性)
        if login_form.is_valid():
            password = login_form.cleaned_data["password"]
            user = UserInfo.objects.get(username=login_form.cleaned_data["username"])
            #user.password =>密文
            #password =>明文
            if check_password(password,user.password):
                print("用户名密码验证成功！")
                # 注意需要把user对象需要能被序列化（json格式）
                request.session['user'] = user.username
                print(request.session["user"])
                # 1. 生成一个随机的sessionid字符串
                # 2. 将sessionid和键值,对保存到本地
                # 3. 通过cookie将sessionid保存到客户端
                # 4. 只可以通过sesssionid来判断当前是哪个用户登录
                return redirect(reverse("forms_base:index"))
            else:
                # 验证失败
                messages.add_message(request, messages.INFO, "用户名密码验证失败")
    return render(request, 'forms_base/login.html', {"form": login_form})


def logout(request):
    print('退出成功')
    return HttpResponse("退出成功")