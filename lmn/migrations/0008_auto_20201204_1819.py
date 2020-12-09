# Generated by Django 3.1.2 on 2020-12-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0007_auto_20201204_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='uuid',
            field=models.CharField(default='0', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
