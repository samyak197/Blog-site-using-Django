# Generated by Django 5.0.1 on 2024-01-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pb_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_published'),
        ),
    ]
