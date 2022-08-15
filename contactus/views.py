from django.contrib import messages
from .forms import ContactUsForm
from .models import ContactUs
from django.shortcuts import redirect
# Create your views here.
def ContactUsView(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print('yyyyyyyyyyyyyyy')
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            ContactUs.objects.create(
                name=name,email=email,message=message
            )
            messages.success(request,'ایمیل شما دریافت شد')
        else:
            messages.success(request,'ایمیل شما دریافت نشد')
    else:
        form = ContactUsForm()
    
    return redirect('/')