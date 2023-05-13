from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(publish_Date__lte=timezone.now()).order_by('publish_Date')
    return render(request, 'budzet/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'budzet/post_detail.html', {'post': post})


