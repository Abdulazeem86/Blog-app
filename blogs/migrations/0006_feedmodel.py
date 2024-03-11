# Generated by Django 5.0.3 on 2024-03-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
