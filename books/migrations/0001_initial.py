# Generated by Django 5.0.1 on 2024-01-24 00:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=25)),
                ('author_f_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('author_prof', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('book_name', models.CharField(max_length=25)),
                ('short_description', models.TextField()),
                ('publisher', models.CharField(max_length=25)),
                ('book_image', models.ImageField(default='default_book_image.jpg', upload_to='media/')),
                ('book_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('isbn', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.authormodel')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.booksmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewBookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField()),
                ('star_given', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=5)])),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.booksmodel')),
            ],
        ),
    ]
