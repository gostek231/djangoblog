from django.shortcuts import render
from django.utils import timezone

from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(publish_Date__lte=timezone.now()).order_by('publish_Date')
    return render(request, 'budzet/post_list.html', {'posts': posts})



