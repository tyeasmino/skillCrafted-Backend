# Generated by Django 5.1.2 on 2024-12-29 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillCrafter', '0004_rename_last_educational_organization_skillcrafter_last_educational_institution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectproposal',
            name='is_completed',
            field=models.CharField(choices=[('2', 'Not Started'), ('1', 'Yes'), ('0', 'No')], default='2', max_length=1),
        ),
    ]