# Generated by Django 2.2.5 on 2019-09-11 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0006_auto_20190911_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitarinfo',
            name='brand_choice',
            field=models.CharField(choices=[('FENDER', 'fender'), ('GIBSON', 'gibson'), ('GRETSCH', 'gretsch'), ('SUHR', 'suhr'), ('IBANEZ', 'ibanez'), ('PRS', 'prs'), ('UNKNOWN', 'unknown'), ('STRANDBERG', 'strandberg'), ('EVH', 'EVH')], default='FND', max_length=10),
        ),
    ]
