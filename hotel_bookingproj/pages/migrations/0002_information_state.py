# Generated by Django 3.1.3 on 2020-11-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='state',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
