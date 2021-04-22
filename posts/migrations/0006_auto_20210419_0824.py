# Generated by Django 3.2 on 2021-04-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210419_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='term',
        ),
        migrations.AddField(
            model_name='definition',
            name='term',
            field=models.ManyToManyField(to='posts.Term'),
        ),
    ]
