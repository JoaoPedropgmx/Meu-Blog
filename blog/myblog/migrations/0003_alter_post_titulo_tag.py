# Generated by Django 4.2.4 on 2023-08-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_post_titulo_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='titulo_tag',
            field=models.CharField(default='My Blog', max_length=255),
        ),
    ]
