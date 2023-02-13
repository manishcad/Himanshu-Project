# Generated by Django 4.2a1 on 2023-02-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0003_anime_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='manga',
            field=models.FileField(default='exit', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anime',
            name='link',
            field=models.URLField(),
        ),
    ]
