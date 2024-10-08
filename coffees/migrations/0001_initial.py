# Generated by Django 4.2.16 on 2024-10-08 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('capacity', models.FloatField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/coffee/')),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('rating', models.FloatField()),
                ('reviewsCount', models.IntegerField()),
                ('coffeeType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffees.type')),
                ('sizes', models.ManyToManyField(blank=True, related_name='coffees', to='coffees.size')),
            ],
        ),
    ]
