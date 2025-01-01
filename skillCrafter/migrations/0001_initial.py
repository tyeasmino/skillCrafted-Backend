# Generated by Django 5.1.2 on 2024-12-19 19:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('skillSeeker', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillCrafter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='skillCrafter/images/skillCrafter/')),
                ('whatsapp', models.CharField(max_length=11)),
                ('linkedin', models.CharField(max_length=50)),
                ('github', models.CharField(max_length=50)),
                ('specialization', models.ManyToManyField(to='skillSeeker.specialization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('★☆☆☆☆', '★☆☆☆☆'), ('★★☆☆☆', '★★☆☆☆'), ('★★★☆☆', '★★★☆☆'), ('★★★★☆', '★★★★☆'), ('★★★★★', '★★★★★')], max_length=10)),
                ('completed_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skillSeeker.skillseeker')),
                ('skillCrafter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skillCrafter.skillcrafter')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal', models.TextField()),
                ('is_proposal_accepted', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('proposed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skillCrafter.skillcrafter')),
            ],
        ),
    ]