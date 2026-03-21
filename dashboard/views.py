from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post
from blog.forms import PostForm

@login_required
def dashboard_home(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'dashboard/index.html', {'posts': posts})


@login_required
def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('dashboard')

    return render(request, 'dashboard/create.html', {'form': form})