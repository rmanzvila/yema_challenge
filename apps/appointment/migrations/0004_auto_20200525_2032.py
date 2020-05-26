# Generated by Django 3.0.6 on 2020-05-26 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]
