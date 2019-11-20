# Generated by Django 2.2.7 on 2019-11-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_magazine_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine_photo',
            name='link',
        ),
        migrations.AddField(
            model_name='magazine_photo',
            name='pdf',
            field=models.FileField(default=6, upload_to='pdf'),
            preserve_default=False,
        ),
    ]
