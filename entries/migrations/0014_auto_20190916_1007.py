# Generated by Django 2.2.5 on 2019-09-16 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0013_guitarinfo_img_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitarinfo',
            name='img_link',
            field=models.CharField(max_length=200),
        ),
    ]
