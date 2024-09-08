# Generated by Django 5.1.1 on 2024-09-04 02:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('smpt_server', models.CharField(max_length=50)),
                ('smpt_port', models.PositiveIntegerField()),
                ('smpt_username', models.CharField(max_length=50)),
                ('smpt_password', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('url_logo', models.CharField(max_length=50)),
                ('app_setting', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_app_setting_id', to='school.appsettingmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
