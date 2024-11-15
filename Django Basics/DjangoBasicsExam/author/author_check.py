from author.models import Author


def author_exists(request):
    return {'author_exists': Author.objects.exists()}