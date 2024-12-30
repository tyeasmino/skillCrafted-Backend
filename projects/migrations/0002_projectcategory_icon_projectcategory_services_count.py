# Generated by Django 5.1.2 on 2024-12-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcategory',
            name='icon',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='projectcategory',
            name='services_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
