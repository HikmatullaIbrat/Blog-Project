from django.urls import path
from . import views
from .views import BlogPostCategoryView, BlogPostListView, BlogPostFeaturedView, BlogPostDetailView

urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('featured', BlogPostFeaturedView.as_view()),
    path('category', BlogPostCategoryView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
    path('blogs/', views.blog_list),
    path('blogs/<int:id>/', views.blog_id_view),
]
