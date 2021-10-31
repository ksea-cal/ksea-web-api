# Generated by Django 3.2.1 on 2021-10-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_semester_term'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'majors',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('ACT', 'Active'), ('ALU', 'Alumni'), ('WAI', 'Waiting'), ('REJ', 'Rejected'), ('SUS', 'Suspended'), ('BAN', 'Banned')], default='WAI', max_length=3),
        ),
    ]
