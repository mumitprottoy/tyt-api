# Generated by Django 4.2.7 on 2023-11-06 02:28

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
            name='ExpertiseField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TherapistWorkplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace', models.CharField(max_length=250)),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='therapists.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='TherapistQualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=250)),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='therapists.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='TherapistProfilePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='therapists.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='TherapistExpertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='therapists.expertisefield')),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='therapists.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='TherapistExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_prof_therapy', models.DateField()),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='therapists.therapist')),
            ],
        ),
    ]
