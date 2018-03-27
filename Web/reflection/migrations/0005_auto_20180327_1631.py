# Generated by Django 2.0.3 on 2018-03-27 06:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reflection', '0004_auto_20180322_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reflection',
            name='grade',
            field=models.PositiveIntegerField(default=1, help_text='Reflect on how well you delivered your product', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
        migrations.AlterField(
            model_name='reflection',
            name='self_plan',
            field=models.TextField(help_text='Detail your three main tasks for the next fortnight', verbose_name='Detail your three main tasks for the next fortnight'),
        ),
        migrations.AlterField(
            model_name='reflection',
            name='self_reflection',
            field=models.TextField(help_text='Reflect on how you delivered on your three main tasks for the last fortnight', verbose_name='Self-reflection'),
        ),
        migrations.AlterField(
            model_name='reflection',
            name='team1_name',
            field=models.CharField(max_length=100, verbose_name='Student 1 Name'),
        ),
        migrations.AlterField(
            model_name='reflection',
            name='team1_reflection',
            field=models.TextField(verbose_name='Evaluation of contribution and performance'),
        ),
        migrations.AlterField(
            model_name='reflection',
            name='team2_name',
            field=models.CharField(max_length=100, verbose_name='Student 2 Name'),
        ),
        migrations.AlterField(
            model_name='reflection',
            name='team2_reflection',
            field=models.TextField(verbose_name='Evaluation of contribution and performance'),
        ),
        migrations.AlterField(
            model_name='reflection',
            name='team3_name',
            field=models.CharField(max_length=100, verbose_name='Student 3 Name'),
        ),
        migrations.AlterField(
            model_name='reflection',
            name='team3_reflection',
            field=models.TextField(verbose_name='Evaluation of contribution and performance'),
        ),
        migrations.AlterField(
            model_name='reflection',
            name='team_number',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='reflection',
            name='title',
            field=models.CharField(max_length=20, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='reflection',
            name='week',
            field=models.IntegerField(blank=True, default=2, null=True, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(12)]),
        ),
    ]
