from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from forumBasics.posts.forms import *
from forumBasics.posts.models import Post


def index(request):
    #
    # form = PersonForm(request.POST or None)
    #
    # if request.method == 'POST':
    #     print(request.POST["person_name"])
    #
    #     if form.is_valid():
    #         print(form.cleaned_data["person_name"])

    context = {
        "my_form": ''
    }

    return render(request, 'base.html', context)


def dashboard(request):
    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == 'GET':
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = posts.filter(title__icontains=query)

    context = {
        "posts": posts,
        "form": form
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostCreateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        "form": form,
    }

    return render(request, 'posts/add-post.html', context)


def edit_post(request, pk):
    return HttpResponse("<h1>Edit Post</h1>") #TODO


def details_page(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post,
    }

    return render(request, 'posts/details-post.html', context)


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == "POST":
        post.delete()
        return redirect('dash')

    context = {
        "form": form,
        "post": post,
    }

    return render(request, 'posts/delete-template.html', context)