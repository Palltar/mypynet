# Generated by Django 3.2.4 on 2021-06-29 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_usernet_users_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernet',
            name='users_media',
            field=models.ManyToManyField(related_name='users', to='profiles.UsersMedia'),
        ),
    ]