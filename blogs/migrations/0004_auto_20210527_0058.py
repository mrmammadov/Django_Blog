# Generated by Django 3.2 on 2021-05-26 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20210527_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('python', 'python'), ('java', 'java'), ('react', 'react')], max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='topics',
        ),
        migrations.CreateModel(
            name='Tag_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ManyToManyField(to='blogs.Post')),
                ('tag_id', models.ManyToManyField(to='blogs.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_id',
            field=models.ManyToManyField(to='blogs.Tag_Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blogs.Tag_Post'),
        ),
    ]
