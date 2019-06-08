# Generated by Django 2.2.1 on 2019-06-07 18:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('dop', models.DateField(default=datetime.date.today)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sale', models.IntegerField()),
                ('ispn', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('price', models.IntegerField()),
                ('copies', models.IntegerField(default=1)),
                ('rate', models.FloatField(default=0, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='book_pics')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.Book')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=1)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Book')),
            ],
        ),
    ]
