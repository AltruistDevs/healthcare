# Generated by Django 4.2.1 on 2023-05-15 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogPage', '0007_alter_blogitem_blog_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogitem',
            name='blog_comments_count',
        ),
    ]