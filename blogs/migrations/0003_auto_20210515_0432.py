# Generated by Django 3.2.2 on 2021-05-15 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210509_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='category_description',
            new_name='category_desc',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='tags',
        ),
        migrations.AlterField(
            model_name='authors',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
