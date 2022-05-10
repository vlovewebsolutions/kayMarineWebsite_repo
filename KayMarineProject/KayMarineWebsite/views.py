from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def AboutUs(request):
    return render(request, 'aboutus.html')

def ContactUs(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # contact_detail = [name, phone, email, message]
        # contact_detail = list(contact_detail[0])
        contact_detail = 'Name: ' + name + '\n' + '\n' + 'Email: ' + str(
            email) + '\n' + 'Message: ' + message
        send_mail(
            'Query of Website Visitor',
            contact_detail,
            'kaymarineservices@gmail.com',
            ['vineetmodi1@gmail.com'],
            fail_silently=False,
        )
        messages.add_message(request, messages.SUCCESS, 'Profile details Sent Successfully.')
        return redirect('ContactUs')
    else:
        return render(request, 'contactus.html', {})
