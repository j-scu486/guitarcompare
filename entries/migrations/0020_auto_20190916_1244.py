# Generated by Django 2.2.5 on 2019-09-16 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0019_auto_20190916_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitarinfo',
            name='brand_choice',
            field=models.CharField(choices=[('FENDER', 'fender'), ('GIBSON', 'gibson'), ('GRETSCH', 'gretsch'), ('SUHR', 'suhr'), ('IBANEZ', 'ibanez'), ('PRS', 'prs'), ('UNKNOWN', 'unknown'), ('STRANDBERG', 'strandberg'), ('EVH', 'EVH'), ('SMITH', 'prs'), ('SCHECTER', 'schecter'), ('TAYLOR', 'taylor'), ('ANDERSON', 'tom anderson'), ('MAYONES', 'mayones'), ('MUSIC', 'musicman')], default='FND', max_length=10),
        ),
    ]
