from django.shortcuts import render,HttpResponse
from .models import UserInfo

# Create your views here.

#django 会给视图传递一个参数（HttpRequest）
def demo(request):

    #最后返回一个HttpResopnse对象
    return  render(request,'app01/demo01.html')

def demo_form(request):
        # print(request.GET)
        # username = request.GET
    username = request.GET.get("email")  #key
    password = request.GET.get("password") #get =>key不存在时候不会报错，返回None

    #最后返回一个HttpResopnse对象
    return  render(request,'app01/demo02_form.html',{'user':username})


def demo_form2(request):
    """
    post提交
    """
    msg = ""
    userlist = {"biubiu@qq.com":"123123",'a@qq.com':"1212"}
    #验证用户登录，验证成功跳转到欢迎您，否则跳转到登录界面
    if request.method =='POST':
        username = request.POST.get("email")  # key
        password = request.POST.get("password")  # get =>key不存在时候不会报错，返回None
        if userlist.get(username)==password:
            return HttpResponse(f'<h2>{username},欢迎你</h2>')
        else:
            msg = "您的密码有误，请重新输入"
    kwgs = {
        "msg":msg
    }
    return render(request,'app01/demo02_form2.html',kwgs)

def demo_form2_db(request):
    """
    post提交
    """
    # userlist = UserInfo.objects.all()  --->取出所有的userInfo object对象
    #验证用户登录，验证成功跳转到欢迎您，否则跳转到登录界面
    msg = ""
    global result
    if request.method =='POST':
        username = request.POST.get("email")  # key
        password = request.POST.get("password")  # get =>key不存在时候不会报错，返回None
        try:
            result = UserInfo.objects.get(email=username)
            if result and result.password == password:
                return HttpResponse(f'<h2>{username},欢迎你</h2>')
            else:
                msg ="用户名密码错误！"
        except UserInfo.DoesNotExist:
            msg = "用户名不存在！"
    kwgs = {
        "msg":msg,
    }
    return render(request,'app01/demo02_form2_db.html',kwgs)
