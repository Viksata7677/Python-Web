from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DetailView, DeleteView

from .models import Post
from .forms import PostForm
from author.models import Author


def dashboard(request):
    posts = Post.objects.all()  # This should retrieve all posts
    return render(request, 'dashboard.html', {'posts': posts})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # Set the author to an existing one, or handle author creation as needed
            author = Author.objects.first()  # Assuming the first author is used
            if not author:
                return redirect('create_author')  # Redirect if no author exists

            # Assign author to the form instance and save
            post = form.save(commit=False)
            post.author = author
            post.save()

            return redirect('dashboard')  # Redirect to the dashboard after saving
    else:
        form = PostForm()
    return render(request, 'post/create-post.html', {'form': form})


def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post/details-post.html', {'post': post})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/edit-post.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post_id = self.kwargs.get("post_id")
        return get_object_or_404(Post, id=post_id)

    def get_success_url(self):
        return reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/delete-post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('dashboard')
