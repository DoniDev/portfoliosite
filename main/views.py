from django.shortcuts import render
from home.models import Greeting, Owner
from about.models import About



def main(request):

    # home
    home = Greeting.objects.first()
    skill1 = home.skills.first()
    skill2 = home.skills.all()[1]
    skill3 = home.skills.all()[2]
    skill4 = home.skills.all()[3]

    # about
    about = About.objects.first()

    context = {
        # home
        'home': home,
        'skill1': skill1,
        'skill2': skill2,
        'skill3': skill3,
        'skill4': skill4,

        # about
        'about': about,



    }


    return render(request, 'main/main.html', context=context)