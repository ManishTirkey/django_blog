from django.shortcuts import render as ren
from django.http import HttpResponse as res, JsonResponse as jres
from .models import allPosts

# Create your views here.


def coverPage(request):
    return ren(request, "coverPage.html")


def Blg(request):
    context = {}
    posts = allPosts.objects.all()
    context['allposts'] = posts
    return ren(request, "blg.html", context=context)


def Blgpost(request, slug):
    context = {}
    post = allPosts.objects.filter(post_id=slug)[0]
    print(post)
    context['post'] = post
    return ren(request, 'bg.html', context=context)

    # return res(f"this is slug : {slug}")
