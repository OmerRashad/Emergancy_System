# Generated by Django 2.2.1 on 2019-06-03 22:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190529_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('content', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Account')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
