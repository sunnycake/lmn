# Generated by Django 3.1.2 on 2020-11-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0004_merge_20201127_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default=None),
        ),
    ]
