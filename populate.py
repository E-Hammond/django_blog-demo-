
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")


from django.utils import timezone
import django
django.setup()

from blogs.models import Categories, Posts, Tags, Authors
import csv

data = []
tags = []
authors = []

with open("Blogentry_Category.csv", newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        data.append(row)

with open("Tags.csv", newline='') as file:
    readr = csv.reader(file, delimiter=',')
    for row in readr:
        tags.append(row)

with open("Authors.csv", newline='') as csvfile:
    read = csv.reader(csvfile, delimiter=',')
    for row in read:
        authors.append(row)


data = data[1:]
tags = tags[1:]
authors = authors[1:]

def create_blog(category,Cat_desc, blogs, body_desc):
    c = Categories.objects.create(category_name=category, category_description=Cat_desc)
    c.save()

    for blog in blogs:
        b = Posts.objects.create(category=c, title=blog, body=body_desc, publication_date=timezone.now())
        b.save()

def create_tags(tag):
    tagg = Tags.objects.create(tag=tag)
    tagg.save()

def create_authors(first_name, last_name, country):
    auth = Authors.objects.create(first_name=first_name, last_name=last_name, country=country)
    auth.save()

def populate_blogs(data,tags,authors):
    for datapoint in data:
        c = datapoint[0]
        t = datapoint[1:5]
        b = datapoint[5]
        c_desc = datapoint[6]

        create_blog(category=c, Cat_desc=c_desc, blogs=t, body_desc=b)

    for i in tags:
        t = i[0]

        create_tags(tag=t)

    for j in authors:
        f = j[0]
        l = j[1]
        count = j[2]

        create_authors(first_name=f, last_name=l, country=count)

populate_blogs(data,tags,authors)

