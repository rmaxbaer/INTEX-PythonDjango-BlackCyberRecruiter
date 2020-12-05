# Generated by Django 3.1.4 on 2020-12-04 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applicant', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.listing'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='skills',
            field=models.ManyToManyField(to='applicant.Skill'),
        ),
    ]
