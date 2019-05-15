from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comments
from .forms import PostForm
from . import urls
import datetime
from django.http import HttpResponse


def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    print(request.POST)
    return render(request, 'blog/post_list.html', {'posts': posts, "x": ".2", "y": [1, 1, 5],
                                                   "description": "Все посты", 'z': datetime.datetime.now(), "True": False, 'f': lambda: 10})  # x,y,z,and сайту не нужны, их можно удалить


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.comments = post.comments().order_by('date')
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if not request.user.is_authenticated:
        return HttpResponse("Ты че сымый умный?")
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, "descript": "Создать пост"})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, "descript": "Изменить пост"})


def add_comm(request):
    if request.user.is_authenticated and request.user.is_active and request.method == "POST":
        form = request.POST
        if form.get('post-id') and form.get('post-id').isnumeric():
            post = Post.objects.filter(pk=int(form.get("post-id")))
            if len(post) == 0:
                return redirect('post_list')
        else:
            return redirect('post_list')

        if form.get('comm-id') and form.get('comm-id').isnumeric():
            comm = Comments.objects.filter(pk=int(form.get("comm-id")))
            if len(comm) == 1:
                returnComm = Comments(author=request.user, text_massage=form.get('text_comm'),
                                      answer_massage=post[0], answer_comment=comm[0])
        else:
            returnComm = Comments(author=request.user, text_massage=form.get('text_comm'),
                                  answer_massage=post[0])

        returnComm.save()

    return redirect('post_detail', pk=post[0].pk)


def post_discus(request):

    posts = Post.objects.filter().order_by('-created_date')
    rez = []
    for p in posts:
        if p.comm_count() > 0:
            rez.append(p)
    posts = rez
    return render(request, 'blog/post_list.html', {'posts': posts, "description": "Обсуждаемое"})


def post_fresher(request):
    posts = Post.objects.filter(
        created_date__gte=datetime.date.today()).order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts, "description": "Свежее"})


def test(request, *c, **d):
    print(d)
    return render(request, 'blog/content_post_only_test.html', {'c': c, "d": d})


def all_comments(request):
    comments = Comments.objects.all().order_by('-date')
    return render(request, 'blog/all_comments.html', {'comments': comments})


def images(request):
    return render(request, 'blog/images.html')
