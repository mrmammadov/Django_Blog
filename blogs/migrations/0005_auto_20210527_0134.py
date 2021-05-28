# Generated by Django 3.2 on 2021-05-26 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20210527_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_id',
        ),
        migrations.AddField(
            model_name='tag',
            name='post_id',
            field=models.ManyToManyField(to='blogs.Post'),
        ),
        migrations.DeleteModel(
            name='Tag_Post',
        ),
    ]
