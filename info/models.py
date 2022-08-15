from django.db import models

# Create your models here.
class Profile(models.Model):
    image = models.ImageField()
    alt = models.CharField(max_length=100)
    name = models.CharField(verbose_name='نام',max_length=200)
    info = models.TextField(verbose_name='توضیحات',)
    resume = models.FileField(verbose_name='رزومه',null=True,blank=True)
    link_resume = models.CharField(verbose_name='ادرس رزومه',max_length=300,blank=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name + " " + self.info
    class Meta:
        verbose_name='پروفایل'
        verbose_name_plural='پروفایل'

class DetailProfile (models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    value = models.CharField(max_length=100,verbose_name='value')
    def __str__(self):
        return self.name + " " + self.value
    class Meta:
        verbose_name='جزيیات پروفایل'
        verbose_name_plural='جزيیات پروفایل'

class Circle(models.Model):
    name = models.CharField(max_length=300,verbose_name='نام')
    number = models.IntegerField(verbose_name='درصد مهارت')
    def __str__(self):
        return self.name + " " + self.number + "%"
    

class Line(models.Model):
    name = models.CharField(max_length=300,verbose_name='نام')
    number = models.IntegerField(verbose_name='درصد مهارت')
    def __str__(self):
        return self.name + " " + self.number + "%"

class Activity(models.Model):
    activity = models.CharField(max_length=300,verbose_name='مهارت ها')
    def __str__(self):
        return self.activity
