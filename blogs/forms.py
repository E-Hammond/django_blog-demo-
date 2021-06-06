
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import SelectDateWidget

from .models import Posts, Categories, Tags, CustomUser



# class UpdatePostForm(forms.ModelForm):
#     title = forms.MultipleChoiceField()
#     body = forms.MultipleChoiceField()
#     publication_date = forms.DateTimeField(widget=SelectDateWidget())
#     class Meta:
#         model = Posts
#         fields = "__all__"
#         exclude = ['slug']

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': 47, 'class':'title'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'size': 30, 'class':'title'}))
    publication_date = forms.DateTimeField(widget=SelectDateWidget())
    # password =forms.CharField(widget= forms.PasswordInput)
    class Meta:
        model = Posts
        fields = '__all__'
        exclude = ['slug']

class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(widget=forms.TextInput(attrs={'size': 38.8, 'class': 'title'}))
    category_description = forms.CharField(widget=forms.Textarea(attrs={'size': 30, 'class': 'desc'}))
    class Meta:
        model = Categories
        fields = '__all__'
        exclude = ['slug']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username','email','password','gender','profile_pic','profile_desc']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ['username', 'email', 'password']
        fields = '__all__'