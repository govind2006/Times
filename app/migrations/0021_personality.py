# Generated by Django 2.2.7 on 2019-11-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_bollywood_buzz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('link', models.URLField(verbose_name='Link')),
                ('Description', models.TextField(verbose_name='Description')),
            ],
        ),
    ]
