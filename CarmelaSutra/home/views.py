from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Min, Sum, Avg
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from uploads.models import Picture, PictureCollection

def index(request):

    collections = PictureCollection.objects.all()
    pictures=Picture.objects.all()

    context = {
        'title': 'kirrrsten',
        'header': 'kirsten becker',
        'collections': collections,
        'pictures': pictures
    }

    return render(request, 'index.html', context)

