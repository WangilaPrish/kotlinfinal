# Generated by Django 5.1.3 on 2024-11-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KotlinApp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('department', models.CharField(max_length=30)),
                ('doctor', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
    ]
