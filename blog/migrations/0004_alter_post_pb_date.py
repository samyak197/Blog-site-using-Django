# Generated by Django 5.0.1 on 2024-01-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_pb_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pb_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
