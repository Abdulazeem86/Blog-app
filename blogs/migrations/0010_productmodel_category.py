# Generated by Django 5.0.3 on 2024-03-15 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_productmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.CharField(default='general', max_length=100),
        ),
    ]
