from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, CommentForm

@login_required
def feed(request):
    following_users = request.user.following.values_list('followed', flat=True)
    posts = Post.objects.filter(author__in=list(following_users) + [request.user.id]).order_by('-created_at')
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
        
    comment_form = CommentForm()
    
    context = {
        'posts': posts,
        'form': form,
        'comment_form': comment_form
    }
    return render(request, 'posts/feed.html', context)

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    return redirect(request.META.get('HTTP_REFERER', 'feed'))
