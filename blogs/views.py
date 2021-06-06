from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Categories, Posts, Authors
from .forms import PostForm, CategoryForm, UserForm, CreateUserForm


# Create your views here.


def home(request):
    categories_list = Categories.objects.all()
    template = 'blog/home.html'
    context = {'categories': categories_list}
    return render(request, template, context)

@login_required(login_url='login')
def detail(request, slug):
    try:
        category = Categories.objects.get(slug=slug)
    except Categories.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'blog/detail.html', {'category': category})


@login_required(login_url='login')
def posts(request):
    posts_list = Posts.objects.all()
    template = 'blog/posts.html'
    context = {'posts': posts_list}
    return render(request, template, context)


@login_required(login_url='login')
def posts_details(request,slug):
    try:
        post = Posts.objects.get(slug=slug)
    except Posts.DoesNotExist:
        raise Http404("Posts does not exist")
    return render(request, 'blog/posts_details.html', {'post': post})

def authors(request):
    authors_list = Authors.objects.all()
    template = 'blog/authors.html'
    context = {'authors': authors_list}
    return render(request, template, context)

def authors_details(request):
    HttpResponse('<h1>This is the authors details<h1/>')

def createblog_form(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        form = PostForm()
    template = 'blog/createpost_form.html'
    context = {'form': form}
    return render(request, template, context)

def category_form(request):
    form = CategoryForm(request.POST)
    if form.is_valid():
        form.save()
        form = CategoryForm()
    template = 'blog/category_form.html'
    context = {'form': form}
    return render(request, template, context)

def edit_post(request, slug):
    posts = Posts.objects.get(slug=slug)
    form = PostForm(instance=posts)

    template = "blog/edit_post.html"
    context = {"post": form}
    render(request,template, context)

def edit_category(request):
    template = "blog/edit_category.html"
    render(request,template)



def UserFormView(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, "Account created for " + user)
        return redirect('login')
        form = UserForm()
    template = 'blog/userform.html'
    context = {'form':form}
    return render(request, template, context)

def Login(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,"Username Or Password incorrect!")
    template = 'blog/reg_index.html'
    context = {'form':form}
    return render(request, template, context)

def LogoutUser(request):
    logout(request)
    return redirect('login')

