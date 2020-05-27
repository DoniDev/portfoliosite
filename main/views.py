from django.shortcuts import render
from home.models import Greeting
from about.models import About
from resume.models import Field
from services.models import Introduction, Service
from projects.models import Project, ProjectIntro


def main(request):

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
    }


    return render(request, 'main/main.html', context=context)