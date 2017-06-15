from django.shortcuts import render, HttpResponse, redirect
from .models import Post


# Create your views here.

def post_list(request):
    post = Post.objects.all()
    # Dic 키값으로 값을 본다.
    context = {
        'posts': post
    }
    return render(request, 'post/post_list.html', context)


def post_delete(request, post_pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        post.delete()
    return redirect('post_list')
