from django.shortcuts import render_to_response
from blog.models import Post

def index(request):
    all_blog_posts = Post.objects.all()
    return render_to_response('blog/index.html', {'all_blog_posts': all_blog_posts})
