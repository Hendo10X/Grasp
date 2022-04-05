
from django.shortcuts import render, redirect
from . forms import SubscibersForm
from . models import subscribers
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SubscibersForm(request.POST )
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed to Graspscience \U0001F642 ' )   
            return redirect('/')     
    else:
        form = SubscibersForm()
    context = {
        'form': form,
    }
    return render(request, 'come/home.html', context)


