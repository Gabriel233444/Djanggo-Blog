# Generated by Django 3.1.7 on 2023-04-05 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/profile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
