# Generated by Django 2.0.3 on 2018-04-01 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_share'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='share_from',
            field=models.CharField(max_length=100),
        ),
    ]
