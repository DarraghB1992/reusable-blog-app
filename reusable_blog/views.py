from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import BlogPostForm
from django.shortcuts import redirect


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "blogdetail.html", {'post': post})


def post_pop(request):
    pop = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:3]
    return render(request, "blogpopular.html", {'pop': pop})


def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)

    else:
        form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
        else:
            form = BlogPostForm(instance=post)
        return render(request, 'blogpostform.html', {'form': form})


def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect(post_list)
