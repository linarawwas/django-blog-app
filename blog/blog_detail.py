from .forms import CommentForm
from .models import Post
from django.shortcuts import render, get_object_or_404

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comments = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            
            new_comment = comment_form.save(commit=False)

            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'new_comments': new_comments,
        'comment_form': comment_form
    }
    return render(request, 'blog_detail.html', context)