from turtle import Turtle
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    image = models.ImageField()
    alt = models.CharField(max_length=100)
    name = models.CharField(verbose_name='نام',max_length=200)
    info = models.TextField(verbose_name='توضیحات',)
    resume = models.FileField(verbose_name='رزومه',null=True,blank=True)
    link_resume = models.URLField(verbose_name='ادرس رزومه',blank=True)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.name + " " + self.info
    class Meta:
        verbose_name='پروفایل'
        verbose_name_plural='پروفایل'

class DetailProfile (models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    value = models.CharField(max_length=100,verbose_name='value')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.name + " " + self.value
    class Meta:
        verbose_name='جزيیات پروفایل'
        verbose_name_plural='جزيیات پروفایل'

class Circle(models.Model):
    name = models.CharField(max_length=300,verbose_name='نام')
    number = models.IntegerField(verbose_name='درصد مهارت')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.name + " " + str(self.number) + "%"
    class Meta:
        verbose_name='نمودار دایره ای'
        verbose_name_plural='نمودار دایره ای'

class Line(models.Model):
    name = models.CharField(max_length=300,verbose_name='نام')
    number = models.IntegerField(verbose_name='درصد مهارت')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.name + " " + str(self.number) + "%"
    class Meta:
        verbose_name='نمودار خطی'
        verbose_name_plural='نمودار خطی'

class Activity(models.Model):
    activity = models.CharField(max_length=300,verbose_name='مهارت ها')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.activity
    class Meta:
        verbose_name='مهارت ها'
        verbose_name_plural='مهارت ها'
