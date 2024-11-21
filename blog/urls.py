from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [   
    path('blog/', views.PostListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)