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
    
    def get_context_data(self, **kwargs):
        # Get the default context
        context = super().get_context_data(**kwargs)

        # Add the three most recent posts excluding the current one
        context['recent_posts'] = Post.objects.exclude(id=self.get_object().id).order_by('-fecha_publicacion')[:3]
        
        return context
    

class PostListByTagView(ListView):
    model = Post
    template_name = 'blog/post_tag_list.html'
    context_object_name = 'posts'
    paginate_by = 10  # Si deseas paginación

    def get_queryset(self):
        tag_name = self.kwargs.get('tag_name')
        return Post.objects.filter(tags__nombre=tag_name).order_by('-fecha_publicacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs.get('tag_name')
        return context