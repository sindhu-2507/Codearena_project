# Generated by Django 2.2.7 on 2019-11-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191124_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='', max_length=100)),
                ('friend', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
    ]