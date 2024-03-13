# Generated by Django 5.0.3 on 2024-03-13 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_rename_feedmodel_postmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]