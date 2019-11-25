# Generated by Django 2.2.7 on 2019-11-24 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191124_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='friend',
        ),
        migrations.AddField(
            model_name='post',
            name='options',
            field=models.PositiveSmallIntegerField(choices=[(1, 'paid by user and split equally'), (2, 'paid by friend and split equally'), (3, 'you owe the full amount'), (4, 'they owe the full amount')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.PositiveSmallIntegerField(choices=[(1, 'food'), (2, 'clothing'), (3, 'groceries'), (4, 'hospital'), (5, 'travel'), (6, 'housing'), (7, 'movies'), (8, 'others')]),
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together={('friend', 'email')},
        ),
    ]
