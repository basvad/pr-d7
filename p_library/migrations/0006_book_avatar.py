# Generated by Django 2.2.6 on 2020-06-28 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_auto_20200618_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='photo'),
        ),
    ]
