# Generated by Django 3.1.7 on 2021-06-03 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drfAPIView', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='image',
        ),
    ]
