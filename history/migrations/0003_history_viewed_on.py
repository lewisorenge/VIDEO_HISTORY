# Generated by Django 3.0.8 on 2020-07-20 22:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_auto_20200721_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='viewed_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
