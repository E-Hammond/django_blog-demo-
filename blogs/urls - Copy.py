
from django.urls import path
from blogs import views

urlpatterns = [
    path('blog/categories/', views.home, name='home'),
    path('blog/categories/<slug>', views.detail, name='detail'),
    path('blog/posts/', views.posts, name='post_home'),
    path('blog/posts/<slug>', views.posts_details, name='posts_details'),
    path('blog/authors/', views.authors),
    path('blog/authors/<slug>', views.authors_details),
    path('blog/posts/new/', views.createblog_form, name='new_post'),
    path('blog/category/new/', views.category_form, name='new_category'),

]
