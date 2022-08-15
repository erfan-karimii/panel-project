from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100,)
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='تگ ها'
        verbose_name_plural='تگ ها'

class SiteSetting(models.Model):
    favicon = models.ImageField()
    alt = models.CharField(max_length=100,verbose_name='توضیحات عکس',null=True)
    tags = models.ManyToManyField(Tag,verbose_name='تگها')
    title_page = models.CharField(max_length=50,null=True)
    text = models.TextField(verbose_name='توضیحات تگ هدر')
    author = models.CharField(max_length=100)
    right = models.CharField(max_length=100,default='تحصیلات',verbose_name='راست')
    left = models.CharField(max_length=100,default='تاریخچه کار',verbose_name='چپ')
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.text

    class Meta:
        verbose_name='تنظیمات سایت'
        verbose_name_plural='تنظیمات سایت'

class Head(models.Model):
    image = models.ImageField(verbose_name='')
    alt = models.CharField(max_length=100,verbose_name='توضیحات عکس',null=True)
    # title = models.CharField(max_length=300,null=True,blank=True)
    # matn_samet = models.CharField(max_length=300,null=True,blank=True,verbose_name='متن ثابت')
    # matn_moteghayer1 = models.CharField(max_length=300,null=True,blank=True,verbose_name='متن متغیر۱')
    # matn_moteghayer2 = models.CharField(max_length=300,null=True,blank=True,verbose_name='متن متغیر۲')
    # matn_moteghayer3 = models.CharField(max_length=300,null=True,blank=True,verbose_name='متن متغیر۳')
    # matn_moteghayer4 = models.CharField(max_length=300,null=True,blank=True,verbose_name='متن متغیر۴')
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True,editable=False)

    
    class Meta:
        verbose_name='قسمت بالایی'
        verbose_name_plural='قسمت بالایی'

class ZirHead(models.Model):
    text_tozih = models.CharField(max_length=100,verbose_name='متن توضیح')
    number = models.IntegerField(verbose_name='مقدار')
    is_more = models.BooleanField(verbose_name='بیشتر از ؟')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.text_tozih
    class Meta:
        verbose_name=' زیر قسمت بالایی'
        verbose_name_plural='زیر قسمت بالایی'

class Khadamat(models.Model):
    title = models.CharField(max_length=100,verbose_name='تیتر')
    text_tozih = models.CharField(max_length=500,verbose_name='متن توضیح')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)

    class Meta:
        verbose_name='خدمات'
        verbose_name_plural='خدمات'

class PricePlan(models.Model):
    title = models.CharField(max_length=100,verbose_name='تیتر')
    is_populer = models.BooleanField(default=False)
    price = models.IntegerField(null=True,blank=True,verbose_name='قیمت')
    time = models.IntegerField(null=True,blank=True,verbose_name='زمان')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    
    class Meta:
        verbose_name='برنامه های قیمت'
        verbose_name_plural='برنامه های قیمت'

class TozihPlan(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    is_active = models.BooleanField(default=False)
    priceplan = models.ForeignKey(PricePlan,on_delete=models.CASCADE,verbose_name='برنامه های قیمت')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='توضیح برنامه های قیمت'
        verbose_name_plural='توضیح برنامه های قیمت'

class Advice(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    image = models.ImageField(verbose_name='عکس')
    alt = models.CharField(max_length=100,verbose_name='توضیحات عکس',null=True)
    text = models.TextField(verbose_name='متن')
    star = models.IntegerField(default=5, validators=[MinValueValidator(1),MaxValueValidator(5)],verbose_name='تعداد ستاره ها')
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)

    class Meta:
        verbose_name='توصیه ها'
        verbose_name_plural='توصیه ها'

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی'

class Product(models.Model):
    image = models.ImageField(verbose_name='عکس')
    alt = models.CharField(max_length=100,verbose_name='توضیحات عکس',null=True)
    title = models.CharField(max_length=100,verbose_name='تیتر')
    text = models.TextField(verbose_name='متن',null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,verbose_name='دسته بندی')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='آثار'
        verbose_name_plural='آثار'

class HistoryRight(models.Model):
    title = models.CharField(max_length=100,verbose_name='تیتر')
    index = models.PositiveIntegerField(verbose_name='ترتیب')
    time = models.CharField(max_length=100,verbose_name='تایم')
    text = models.TextField(verbose_name='متن')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='تاریچه سمت راست'
        verbose_name_plural='تاریچه سمت راست'

class HistoryLeft(models.Model):
    title = models.CharField(max_length=100,verbose_name='تیتر')
    index = models.PositiveIntegerField(verbose_name='ترتیب')
    time = models.CharField(max_length=100,verbose_name='تایم')
    text = models.TextField(verbose_name='متن')
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='تاریچه سمت چپ'
        verbose_name_plural='تاریچه سمت چپ'

class Call(models.Model):
    country = models.CharField(max_length=100,null=True,blank=True,verbose_name='کشور')
    city = models.CharField(max_length=100,null=True,blank=True,verbose_name='شهر')
    street = models.CharField(max_length=100,null=True,blank=True,verbose_name='خیابان')
    post = models.EmailField(max_length=100,null=True,blank=True,verbose_name='ایمیل')
    telegram = models.CharField(max_length=100,null=True,blank=True,verbose_name='تلگرام')
    skype = models.CharField(max_length=100,null=True,blank=True,verbose_name='اسکایپ')
    poshtebany = models.CharField(max_length=100,null=True,blank=True,verbose_name='پشتیبانی')
    daftar = models.CharField(max_length=100,null=True,blank=True,verbose_name='دفتر')
    shakhsy = models.CharField(max_length=100,null=True,blank=True,verbose_name='تلفن شخصی')
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)

    class Meta:
        verbose_name='اطلاعات تماس'
        verbose_name_plural='اطلاعات تماس'

