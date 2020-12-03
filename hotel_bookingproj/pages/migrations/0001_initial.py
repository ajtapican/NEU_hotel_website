# Generated by Django 3.1.3 on 2020-12-03 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('phone', models.PositiveIntegerField(default=False)),
            ],
        ),
    ]
