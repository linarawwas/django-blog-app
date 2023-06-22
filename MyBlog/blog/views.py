from django.views.generic import ListView, DetailView
from .models import Post
from .forms import CommentForm, BlogForm
from django.shortcuts import render

class BlogList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2
    
class BlogDetail(DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comments = post.comments.filter(active=True)
        new_comment = None

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()  # Reset the form after successful submission

        context = {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form
        }
        return render(request, self.template_name, context)
    from django.http import HttpResponse

def CreateBlogPost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('New blog successfully added!')
    else:
        form = BlogForm()
        context = {
            'form': form
        }
    return render(request, 'create_blog.html', context)