from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Like, Follow
from posts.models import Post
from users.models import User

@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect(request.META.get('HTTP_REFERER', 'feed'))

@login_required
def toggle_follow(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    if user_to_follow != request.user:
        follow, created = Follow.objects.get_or_create(follower=request.user, followed=user_to_follow)
        if not created:
            follow.delete()
    return redirect(request.META.get('HTTP_REFERER', 'profile'))
