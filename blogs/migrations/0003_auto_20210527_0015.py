# Generated by Django 3.2 on 2021-05-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210517_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topics',
            field=models.CharField(default='programming', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
