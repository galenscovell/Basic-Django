from django.shortcuts import render, get_object_or_404
# import Post model from current dir
from .models import Post

def post_list(request):
    # create variable for QuerySet
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    # render template with 'posts' object as dynamic data
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
