from django.urls import path

from .views import BlogPageView, AboutPageView, BlogDetailView, BlogCreateView,BlogUpdateView, BlogDeleteView

urlpatterns=[
    path('', BlogPageView.as_view(), name='main-home'),
    path('about/', AboutPageView.as_view(), name='home-about'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]