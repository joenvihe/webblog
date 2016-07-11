from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    # Se adiciona el posts
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # Se envia la variable posts
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    # Post.objects.get(pk=pk) no se usa porque si PK es vacio saldra error.