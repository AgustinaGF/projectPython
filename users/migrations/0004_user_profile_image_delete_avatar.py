# Generated by Django 4.0.5 on 2022-07-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_profile_image_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(default=1, upload_to='profile_image'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]