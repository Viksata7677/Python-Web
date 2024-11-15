from django.views.generic import DetailView

from author.forms import AuthorForm
from author.models import Author
from posts.models import Post
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, 'index.html')


def create_author(request):

    if Author.objects.exists():
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AuthorForm()

    return render(request, 'author/create-author.html', {'form': form})


class ProfileDetailView(DetailView):
    model = Author
    template_name = 'author/details-author.html'  # Path to your template
    context_object_name = 'author'  # This will be accessible in the template as 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_updated_post'] = self.object.posts.last() if self.object.posts.exists() else None
        return context


def edit_author(request):
    author = Author.objects.first()  # Get the first author in the database

    if author is None:
        return redirect('create_author')  # Redirect to a create author view if no authors exist

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('details_author')  # Redirect to the author's profile details page (you may want to change this)
    else:
        form = AuthorForm(instance=author)  # Pre-fill the form with author's current data

    return render(request, 'author/edit-author.html', {'form': form, 'author': author})


def delete_author(request):
    author = get_object_or_404(Author)
    if request.method == 'POST':
        author.delete()
        return redirect('index')


def dashboard(request):
    return render(request, 'dashboard.html')
