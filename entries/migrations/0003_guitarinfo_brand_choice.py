# Generated by Django 2.2.5 on 2019-09-09 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20190908_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitarinfo',
            name='brand_choice',
            field=models.CharField(choices=[('FND', 'fender'), ('GIB', 'gibson'), ('GRT', 'gretsch'), ('SUH', 'suhr'), ('IBZ', 'ibanez'), ('PRS', 'prs'), ('UKN', 'unknown')], default='FND', max_length=3),
        ),
    ]
