# Generated by Django 4.1.7 on 2024-03-20 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_categorymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='category',
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]