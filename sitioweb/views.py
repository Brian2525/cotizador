from django.shortcuts import render

# Create your views here.




def index(request):
    return render(request, 'sitioweb/index.html')

def privacy(request):
    return render(request, 'sitioweb/privacy.html')