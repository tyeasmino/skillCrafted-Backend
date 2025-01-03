# Generated by Django 5.1.2 on 2024-12-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillCrafter', '0002_skillcrafter_curriculum_vitae_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillcrafter',
            old_name='passing_year',
            new_name='last_passing_year',
        ),
        migrations.RenameField(
            model_name='skillcrafter',
            old_name='result',
            new_name='last_result',
        ),
        migrations.AlterField(
            model_name='skillcrafter',
            name='curriculum_vitae',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
