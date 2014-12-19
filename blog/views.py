from django.shortcuts import render
# import Post model from current dir
from .models import Post

def post_list(request):
    # create variable for QuerySet
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
