# Generated by Django 4.2.4 on 2023-09-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=230)),
                ('img', models.ImageField(upload_to='teampic')),
                ('desc', models.TextField()),
            ],
        ),
    ]
