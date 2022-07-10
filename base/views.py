from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .forms import ContactForm
from django.contrib import messages
import sweetify

from .models import Profile ,SocialLink,Interest,Service,Certifcation, Testimonial,Experience,Education,Project ,Contact
# Create your views here.
def index(request):
    info=Profile.objects.all().first()
    links=SocialLink.objects.all()
    interest=Interest.objects.all()
    testimonial=Testimonial.objects.all()
    experince=Experience.objects.all()
    edu=Education.objects.all()
    project=Project.objects.all()
    service=Service.objects.all()
    certifcation=Certifcation.objects.all()
    form=ContactForm()
    if request.method == 'POST':
        form=ContactForm(request.POST)   
        if form.is_valid():
            form.save()
            sweetify.success(request , "the message is sent successfully")
        else:
            sweetify.error(request, 'An error occurred while sending the message')

    context={
        'info':info,
        'links':links,
        'interest':interest,
        'testimonial':testimonial,
        'experince':experince,
        'edu':edu,
        'project':project,
        'form':form,
        'service':service,
        'certifcation':certifcation
    }

    return render(request,'index.html', context=context)
