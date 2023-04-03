# Generated by Django 4.1.7 on 2023-03-08 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Price', models.IntegerField()),
                ('Image', models.ImageField(upload_to='pictures')),
                ('User', models.CharField(max_length=50)),
                ('Contact', models.TextField()),
            ],
        ),
    ]