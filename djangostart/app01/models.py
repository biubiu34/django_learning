from django.db import models

# Create your models here.


#class定义的一个类就是一个表
class UserInfo(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username