# Generated by Django 4.0 on 2022-06-12 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
    ]