from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    """注册表单"""
    username = forms.CharField(label="用户名", max_length=30, widget=forms.TextInput(attrs={"size":20,}))
    email = forms.EmailField(label="邮 箱", max_length=30, widget=forms.TextInput(attrs={"size":20,}))
    password1 = forms.CharField(label="密码1", max_length=30, widget=forms.PasswordInput(attrs={"size":20,}))
    password2 = forms.CharField(label="密码2", max_length=30, widget=forms.PasswordInput(attrs={"size":20,}))

    def clean_username(self):
        '''验证重复昵称，需要返回字段值'''
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        raise forms.ValidationError("该昵称已被占用，请使用其他的昵称")

    def clean_email(self):
        '''验证重复email，需要返回字段值'''
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError("该邮箱已经被使用请使用其他的")

    def clean(self):
        """
        验证两次输入的密码是否一致
        不需要自己返回数据
        """
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        print(password2, password1)
        if password1 != password2:
            raise forms.ValidationError("两次输入的密码不一致")


class LoginForm(forms.Form):
    """登录表单"""
    username = forms.CharField(label="用户名", max_length=30, widget=forms.TextInput(attrs={"size": 20, }))
    password = forms.CharField(label="密  码", max_length=30, widget=forms.PasswordInput(attrs={"size": 20, }))