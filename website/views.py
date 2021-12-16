from django.shortcuts import render, redirect
from django.utils.html import format_html
from django.contrib import messages
from website.forms import ContactForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from .forms import SubscriberForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# Create your views here.
def home(request):
    context = {
        'nbar': 'home',
    }
    return render(request, 'home.html', context)

def services(request):
    context = {
        'nbar': 'services',
    }
    return render(request, 'services.html', context)

def realisation(request):
    context = {
        'nbar': 'realisation',
    }
    return render(request, 'realisation.html', context)

def contact(request):
    context = {
        'nbar': 'contact',
        'modelform': ContactForm,
    }
    return render(request, 'contact.html', context)

def GetMessage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Test for msg if email field is empty
            if email == None:
                email = "Non Fourni"
                msg = "Si vous recevez ce mail c'est que votre message a bien été envoyé et est en cours de traitement. Voici les détails de votre message:..." + "\n\nNom Complet: " + name + "\nNuméro de téléphone : " + str(phone) + "\n\nMessage Envoyé : " + message + "\n\n\nMerci de nous avoir contacté. Nous espérons vous revoir très bientôt.\n\nTel : 656997810\nEmail : joefah2003@gmail.com\n\nEcrivez nous à propos de tout ce que vous voulez, a n'importe quel moment comme bon vous semble!"
            subjectEmail = subject + " <" + f'{email}' + ">"

            # Uncomment this later to send email to required address
            # try:
            #     send_mail(
            #         subjectEmail, #subject
            #         msg, #message
            #         email, #from email
            #         ['joelfah2003@gmail.com', email], #to email
            #         )
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found')

            # Save message in Database
            # form.save()

            # Test if form data was saved and output corresponding flash message to confirm message placement or not.
            try:
                form.save()
                message_out_success = format_html(
                    f'Thanks for contacting us, <strong> {name} </strong> ! Your message has been sent successfully. You will be email a copy at <strong> {email}</strong>. Feel free to fill the form again if you wish.'
                )
                messages.success(
                    request,
                    message_out_success
                )
            except:
                message_out_error = format_html(
                   f'Sorry, <strong> {name} </strong> ! There was a problem sending your message. Please reload and try again!'
                )
                messages.error(
                    request,
                    message_out_error
                )
            
            # Redidrect to the same page with message output.
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'modelform': ContactForm
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'nbar': 'about',
    }
    return render(request, 'about.html', context)

def serviceDetails(request):
    context = {
        'nbar': 'serviceDetails'
    }
    return render(request, 'services-detail.html', context)




def random_digits(): 
    return "%0.12d" % random.randint(0, 999999999999) 

@csrf_exempt 
def new(request): 
    if request.method == 'POST': 
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits()) 
        sub.save()
        message = Mail(
        from_email=settings.FROM_EMAIL, 
        to_emails=sub.email,
        subject='Newsletter Confirmation',
        html_content='Thank you for signing up for my email newsletter! \ Please complete the process by \ <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \ confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'), sub.email, sub.conf_num)) 
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message) 
        context = {
            'email': sub.email,
            'action': 'added',
            'form': SubscriberForm()
        }
        return render(request, 'email-news.html', context) 
    else: 
        context = {
            'form': SubscriberForm()
        }
        return render(request, 'email-news.html', context)

def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True 
        sub.save()
        context = {
            'email': sub.email,
            'action': 'confirmed'
        }
        return render(request, 'email-news.html', context) 
    else: 
        context = {
            'email': sub.email,
            'action': 'denied'
        }
        return render(request, 'email-news.html', context)