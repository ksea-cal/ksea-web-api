# Generated by Django 3.2.1 on 2021-05-16 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210516_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('term', models.CharField(choices=[('spr', 'spring'), ('fal', 'fall')], max_length=3)),
            ],
            options={
                'db_table': 'semesters',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('ACT', 'Active'), ('SUS', 'Suspended'), ('BAN', 'Banned')], default='ACT', max_length=3),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('role', models.CharField(choices=[('GEN', 'General member'), ('BOA', 'Board member')], default='GEN', max_length=3)),
                ('paid_membership_fee', models.BooleanField(default=False)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to='core.semester')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profiles',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='core.userprofile')),
            ],
            options={
                'db_table': 'logs',
            },
        ),
    ]