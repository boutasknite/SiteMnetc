from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def Index(request):
    thrusts = Thrust.objects.all()
    members = Member.objects.all()
    context = {"thrusts":thrusts, "nb_thrusts":len(thrusts), "members":members, "nb_members":len(members)}
    return render(request, 'index.html', context)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'login.html')


def Join_us(request):
    return render(request, 'join_us.html')


@csrf_exempt
def Save_Application(request):
    first_name = request.POST.get('first_name')
    second_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')
    affiliation = request.POST.get('affiliation')
    research_area = request.POST.get('research_area')
    position = request.POST.get('position')
    cv_file = request.FILES.get('cv')
    motivation = request.POST.get('motivation')
    contribution = request.POST.get('contribution')
    references = request.POST.get('references')
    Demand.objects.create(
        First_Name=first_name,
        Second_Name=second_name,
        Email=email,
        Phone_Number=phone_number,
        Affiliation=affiliation,
        CV=cv_file,
        Research_Area=research_area,
        Position=position,
        Motivation=motivation,
        Contribution=contribution,
        References=references
    )
    return HttpResponse("ok")


def Profile(request):
    return render(request, 'profile.html')


