from django.utils import timezone
import django
django.setup()

from blogs.models import Categories, Posts, Tags, Authors

# import your libraries
import pandas as pd
from faker import Faker
import random

data = []

# Create a function to generate post

def generate_posts(n):
    # Create containers for fields
    global authors, titles, bodies, df, category, categories
    authors = []
    titles = []
    bodies = []
    categories = ['politics', 'business', 'health', 'environment', 'arts']
    # Create faker instance
    fake = Faker()
    # Append fake generated values to containers
    for element in range(n):
        authors.append(fake.name())
        titles.append(fake.sentence())
        bodies.append(fake.text())
    df = pd.DataFrame(zip(authors, titles, bodies), columns=['Author', 'Title', 'Body'])
    df['Category'] = df['Title'].apply(lambda x: random.choice(categories))
    category = df.Category.to_list()

generate_posts(20)

for el in range(len(df)):
    lis = df.iloc[el].to_list()
    data.append(lis)

def create_blog(category, blogs, body_desc):
    c = Categories.objects.create(category_name=category)
    c.save()

    for blog in blogs:
        b = Posts.objects.create(category=c, title=blog, body=body_desc, publication_date=timezone.now())
        b.save()

# def create_tags(tag):
#     tagg = Tags.objects.create(tag=tag)
#     tagg.save()
#
# def create_authors(first_name, last_name, country):
#     auth = Authors.objects.create(first_name=first_name, last_name=last_name, country=country)
#     auth.save()

def populate_blog(data):
    for datapoint in data:
        c = datapoint[3]
        p = data[1]
        desc = datapoint[2]



        create_blog(category= c, blogs=p, body_desc=desc)

populate_blog(data)




