# Generated by Django 4.1.5 on 2023-01-29 16:14

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import media_docs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('about', ckeditor.fields.RichTextField()),
                ('author', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('image', models.ImageField(upload_to=media_docs.models.file_path)),
                ('file', models.FileField(upload_to=media_docs.models.file_path)),
                ('tags', models.ManyToManyField(to='media_docs.tags')),
                ('uploaded_by', models.ForeignKey(help_text='Который добавил на сайт объект', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Comics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('about', ckeditor.fields.RichTextField()),
                ('author', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('image', models.ImageField(upload_to=media_docs.models.file_path)),
                ('file', models.FileField(upload_to=media_docs.models.file_path)),
                ('tags', models.ManyToManyField(to='media_docs.tags')),
                ('uploaded_by', models.ForeignKey(help_text='Который добавил на сайт объект', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комикс',
                'verbose_name_plural': 'Комиксы',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('about', ckeditor.fields.RichTextField()),
                ('author', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('image', models.ImageField(upload_to=media_docs.models.file_path)),
                ('file', models.FileField(upload_to=media_docs.models.file_path)),
                ('tags', models.ManyToManyField(to='media_docs.tags')),
                ('uploaded_by', models.ForeignKey(help_text='Который добавил на сайт объект', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_set', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]