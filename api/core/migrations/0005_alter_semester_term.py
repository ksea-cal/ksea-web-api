# Generated by Django 3.2.1 on 2021-05-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210519_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='term',
            field=models.CharField(choices=[('spring', 'spring'), ('fall', 'fall')], max_length=10),
        ),
    ]