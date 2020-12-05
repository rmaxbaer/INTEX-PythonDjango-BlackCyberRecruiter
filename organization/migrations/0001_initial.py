# Generated by Django 3.1.4 on 2020-12-04 23:42

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applicant', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('contract_type', models.CharField(max_length=50)),
                ('compensation', models.CharField(max_length=50)),
                ('relocation_assistance', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('company_name', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=4)),
                ('sectors', models.CharField(max_length=4)),
                ('description', models.TextField()),
                ('date_founded', models.DateField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateTimeField()),
                ('start_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.applicant')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.position')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
        migrations.AddField(
            model_name='listing',
            name='skills',
            field=models.ManyToManyField(to='applicant.Skill'),
        ),
    ]
