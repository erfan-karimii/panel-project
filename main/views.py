from django.shortcuts import render
from .models import *
from contactus.forms import ContactUsForm
from info.models import *
# Create your views here.
def home(request,id):
    context = {
    'tags':Tag.objects.filter(owner_id = id),
    'sitesetting':SiteSetting.objects.filter(active=True,owner_id = id).last(),
    'head':Head.objects.filter(active=True,owner_id = id).last(),
    'zirheads':ZirHead.objects.filter(owner_id = id),
    'khadamats':Khadamat.objects.filter(owner_id = id),
    'priceplans':PricePlan.objects.filter(owner_id = id),
    'tozihplans':TozihPlan.objects.filter(owner_id = id),
    'advice': Advice.objects.filter(active=True,owner_id = id).last(),
    'categorys':Category.objects.filter(owner_id = id),
    'products':Product.objects.filter(owner_id = id),
    'historyrights':HistoryRight.objects.filter(owner_id = id).order_by('-index'),
    'historylefts':HistoryLeft.objects.filter(owner_id = id).order_by('-index'),
    'call':Call.objects.filter(active=True,owner_id = id).last(),
    'form':ContactUsForm(),
    'Profile': Profile.objects.filter(active=True,owner_id = id).last(),
    'DetailProfile': DetailProfile.objects.filter(owner_id = id),
    'Circle': Circle.objects.filter(owner_id = id),
    'Line': Line.objects.filter(owner_id = id),
    'Activity': Activity.objects.filter(owner_id = id),
    }
    return render(request,'index.html',context)
