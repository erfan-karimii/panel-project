from django.shortcuts import render
from .models import *
from contactus.forms import ContactUsForm
from info.models import *
# Create your views here.
def home(request):
    context = {
    'tags':Tag.objects.all(),
    'sitesetting':SiteSetting.objects.filter(active=True).last(),
    'head':Head.objects.filter(active=True).last(),
    'zirheads':ZirHead.objects.all(),
    'khadamats':Khadamat.objects.all(),
    'priceplans':PricePlan.objects.all(),
    'tozihplans':TozihPlan.objects.all(),
    'advice': Advice.objects.filter(active=True).last(),
    'categorys':Category.objects.all(),
    'products':Product.objects.all(),
    'historyrights':HistoryRight.objects.all().order_by('-index'),
    'historylefts':HistoryLeft.objects.all().order_by('-index'),
    'call':Call.objects.filter(active=True).last(),
    'form':ContactUsForm(),
    'Profile': Profile.objects.filter(active=True).last(),
    'DetailProfile': DetailProfile.objects.all(),
    'Circle': Circle.objects.all(),
    'Line': Line.objects.all(),
    'Activity': Activity.objects.all(),
    }
    return render(request,'index.html',context)
