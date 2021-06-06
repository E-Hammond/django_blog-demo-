
from django.urls import path
from blogs import views

urlpatterns = [
    path('blog/categories/', views.home, name='home'),
    path('blog/userform/', views.UserFormView, name = 'userform'),
    path('blog/login/', views.Login, name='login'),
    path('blog/logout/', views.LogoutUser, name='logout'),
    path('blog/categories/<slug>', views.detail, name='detail'),
    path('blog/posts/', views.posts, name='post_home'),
    path('blog/posts/<slug>', views.posts_details, name='posts_details'),
    path('blog/authors/', views.authors),
    path('blog/authors/<slug>', views.authors_details),
    path('blog/posts/new/', views.createblog_form, name='new_post'),
    path('blog/categories/new/', views.category_form, name='new_category'),
    path('blog/posts/<slug>', views.edit_post, name="edit_post"),
    path('blog/categories/<slug>/edit/', views.edit_category, name="edit_category")
]
