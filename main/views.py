from django.shortcuts import render, redirect
from home.models import Greeting
from about.models import About
from resume.models import Field
from services.models import Introduction, Service
from projects.models import Project, ProjectIntro
from contact.models import Contact
from contact.forms import ContactForm
from django.core.mail import send_mail
import os
from django.contrib import messages



def main(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['name']
        from_email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        send_mail(subject, message, from_email, [os.environ.get(str('EMAIL_USER'))])
        messages.success(request, 'Message sent')
        form = ContactForm()
        return redirect('/')




    # home
    home = Greeting.objects.first()
    skill1 = home.skills.first()
    skill2 = home.skills.all()[1]
    skill3 = home.skills.all()[2]
    skill4 = home.skills.all()[3]

    # about
    about = About.objects.first()

    # resume
    fields = Field.objects.all()

    # services
    introduction = Introduction.objects.first()
    services = Service.objects.all()

    # projects
    printro = ProjectIntro.objects.first()
    projects = Project.objects.all()

    # contact
    contact = Contact.objects.first()

    context = {
        # home
        'home': home,
        'skill1': skill1,
        'skill2': skill2,
        'skill3': skill3,
        'skill4': skill4,

        # about
        'about': about,

        # resume
        'fields': fields,

        # services
        'introduction': introduction,
        'services': services,

        # projects
        'printro': printro,
        'projects': projects,

        # contact
        'contact': contact,
        'form': form,
    }


    return render(request, 'main/main.html', context=context)

