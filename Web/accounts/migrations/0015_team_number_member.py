# Generated by Django 2.0.1 on 2018-05-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20180504_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='number_member',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
