# Generated by Django 2.2.5 on 2019-09-16 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0012_auto_20190913_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitarinfo',
            name='img_link',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
