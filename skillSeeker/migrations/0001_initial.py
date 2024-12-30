# Generated by Django 5.1.2 on 2024-12-19 19:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SkillSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='skillSeeker/images/skillSeeker/')),
                ('company_name', models.CharField(max_length=100)),
                ('company_started', models.CharField(max_length=20)),
                ('company_employee', models.IntegerField()),
                ('company_address', models.CharField(max_length=200)),
                ('company_website', models.CharField(max_length=100)),
                ('company_logo', models.ImageField(upload_to='skillSeeker/images/company')),
                ('whatsapp', models.CharField(blank=True, max_length=11, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=50, null=True)),
                ('github', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.ManyToManyField(to='skillSeeker.designation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('specialization', models.ManyToManyField(to='skillSeeker.specialization')),
            ],
        ),
    ]
