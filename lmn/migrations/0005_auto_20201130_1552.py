# Generated by Django 3.1.3 on 2020-11-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0004_merge_20201130_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='rating',
            field=models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default=5),
        ),
    ]