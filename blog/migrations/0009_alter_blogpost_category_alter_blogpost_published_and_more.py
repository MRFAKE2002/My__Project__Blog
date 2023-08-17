# Generated by Django 4.1.7 on 2023-04-10 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_category_alter_blogpost_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='blog.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 10, 7, 22, 11, 625123, tzinfo=datetime.timezone.utc), verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='blogpostcomment',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 10, 7, 22, 11, 627123, tzinfo=datetime.timezone.utc), verbose_name='published'),
        ),
    ]