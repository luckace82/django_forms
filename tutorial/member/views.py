from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .forms import NameForm
from django.core.mail import send_mail
def get_name(request):
    #if this is a POST request we need to process the form data
    if request.method=="POST":
        #create a form instance and populate it with data from the request
        form=NameForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            cc_myself = form.cleaned_data["cc_myself"]

            recipients = ["info@example.com"]
            if cc_myself:
                recipients.append(sender)

                send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect("/thanks/")
    else:
        form=NameForm()
    return render(request,"name.html",{"form":form})    
            
            