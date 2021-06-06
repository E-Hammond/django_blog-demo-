from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils.text import slugify
from django.utils import timezone


class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=False, null=False)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super(Categories, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '{}/{}/'.format('/blog', self.slug)



class Tags(models.Model):
    # tag_id = models.CharField(max_length=20, primary_key=True)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return '{}/{}/'.format('/blog', self.slug)



class Posts(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=150, blank=False)
    body = models.CharField(max_length=500, blank=False, verbose_name='Description')
    publication_date = models.DateTimeField("Published")

    slug = models.SlugField(max_length=255, unique=False, null=False)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '{}/{}/'.format('/blog', self.slug)



class Authors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return '{}/{}/'.format('/blog', self.slug)

class CustomUser(User):
    gender_list = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    user_name = models.CharField(max_length=100)

    gender = models.CharField(max_length=2, choices=gender_list, default='Male')
    profile_pic = models.ImageField(upload_to='Media/profile_pics', blank=True)
    profile_desc = models.TextField(max_length=200)


    def __str__(self):
        return self.user_name
