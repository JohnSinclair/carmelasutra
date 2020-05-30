from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Min, Sum, Avg
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from uploads.models import Picture, PictureCollection, CourseOfLife


def view_pic_collection(request, pk):
    """
    Return data for dashboard page

    """
    collection = PictureCollection.objects.get(pk=pk)
    print(collection.pictures.all())

    context = {
        'title': 'kirrrsten',
        'header': 'kirsten becker',
        'collection_title': collection.name,
        'collection': collection
    }

    return render(request, 'picture_collection.html', context)


def view_cv(request):
    """
    Return data for dashboard page

    """
    cv = CourseOfLife.objects.all().order_by('created_at')[0]
    

    context = {
        'title': 'kirrrsten',
        'header': 'kirsten becker',
        'cv': cv,
        
    }
    # add_header X-Frame-Options SAMEORIGIN always;
 
    return render(request, 'cv.html', context)


def view_gallery(request, pk):
    """
    Return data for dashboard page

    """
    collection = PictureCollection.objects.get(pk=pk)
    

    context = {
        'title': 'kirrrsten',
        'header': 'kirsten becker',
        'collection': collection,
        
    }
    # add_header X-Frame-Options SAMEORIGIN always;
 
    return render(request, 'gallery.html', context)

