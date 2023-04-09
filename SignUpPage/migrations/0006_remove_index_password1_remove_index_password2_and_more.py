# Generated by Django 4.2 on 2023-04-09 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SignUpPage', '0005_remove_index_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='index',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='index',
            name='username',
        ),
        migrations.AddField(
            model_name='index',
            name='bio',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='index',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
        migrations.AddField(
            model_name='index',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]