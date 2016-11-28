# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 04:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField()),
                ('birthdate', models.DateField(null=True)),
                ('city_of_birth', models.CharField(blank=True, max_length=255)),
                ('state_of_birth', models.CharField(blank=True, max_length=150)),
                ('country_of_birth', models.CharField(blank=True, max_length=255)),
                ('sex_at_birth', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('eye_color', models.CharField(choices=[('Black', 'Black'), ('Blue', 'Blue'), ('Brown', 'Brown'), ('Gray', 'Gray'), ('Green', 'Green'), ('Hazel', 'Hazel'), ('Other', 'Other')], max_length=10)),
                ('mother_first_name', models.CharField(blank=True, max_length=150)),
                ('mother_maiden_name', models.CharField(blank=True, max_length=150)),
                ('mother_last_name', models.CharField(blank=True, max_length=150)),
                ('father_first_name', models.CharField(blank=True, max_length=150)),
                ('father_last_name', models.CharField(blank=True, max_length=150)),
                ('birth_hospital', models.CharField(blank=True, max_length=150)),
                ('searching_for', models.CharField(choices=[('Cousin', 'Cousin'), ('Child', 'Child'), ('Parent', 'Parent'), ('Sibling', 'Sibling')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='')),
                ('description', models.CharField(blank=True, max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(default='picture.png', upload_to='')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, max_length=25)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('relationship', models.CharField(blank=True, max_length=30)),
                ('birth_year', models.IntegerField(null=True)),
                ('unique_id', models.CharField(blank=True, max_length=100)),
                ('location', models.TextField(blank=True)),
                ('family_surnames', models.TextField(blank=True)),
                ('similarity', models.CharField(blank=True, max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
