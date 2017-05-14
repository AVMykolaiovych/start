from django.shortcuts import render

from django.shortcuts import render_to_response

from django.http import HttpResponse


from .models import Post

from django.shortcuts import get_object_or_404

# Create your views here.


def posthome(request):
    content = {
        "title": "The list of books"
    }
    return render(request, "index.html", content)

def postcreate(request):
    content = {
        "title": "The list of books create"
    }
    return render(request, "index.html", content)

def postdetail(request, id=None):
    # instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post, id=id)

    content = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "booksdetail.html", content)

def postlist(request):
    querybook = Post.objects.all
    content = {
        "title": "The list of books list",
        "object_list": querybook,
    }
    return render(request, "index.html", content)

def postupdate(request):
    content = {
        "title": "The list of books update"
    }
    return render(request, "index.html", content)

def postdelete(request):
    content = {
        "title": "The list of books delete"
    }
    return render(request, "index.html", content)