# Generated by Django 4.2a1 on 2023-02-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0007_mangafiles_anime_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='mangafiles',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
