from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Post, Categoria, Tag

# Vista para listar todos los posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10  # Número de posts por página

    def get_queryset(self):
        return Post.objects.all().order_by('-fecha_publicacion')

# Vista para mostrar el detalle de un post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self):
        # Recuperar post usando slug o id (puedes ajustar según tu modelo)
       return get_object_or_404(Post, slug=self.kwargs.get('slug'))