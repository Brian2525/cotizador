from django.shortcuts import render, redirect
from blog.models import Post
from clientes.forms import ContactForm

# Create your views here.




def index(request):
    recent_posts = Post.objects.order_by('-fecha_publicacion')[:3]
    print("inicio")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("is valid")
            form.save()
            return redirect('index')  
    else:
        print("Aun no hay datos")
        form = ContactForm()
    return render(request, 'sitioweb/index.html', {'recent_posts': recent_posts, 'form': form })


def privacy(request):
    return render(request, 'sitioweb/privacy.html')
