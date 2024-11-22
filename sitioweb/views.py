from django.shortcuts import render
from blog.models import Post

# Create your views here.




def index(request):
    recent_posts = Post.objects.order_by('-fecha_publicacion')[:3]
    return render(request, 'sitioweb/index.html', {'recent_posts': recent_posts})

def privacy(request):
    return render(request, 'sitioweb/privacy.html')