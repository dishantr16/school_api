# Generated by Django 3.2.3 on 2021-12-06 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'subject group',
                'verbose_name_plural': 'subject groups',
                'db_table': 'subjectgroup',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.subject_group')),
                ('subject_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.classes')),
            ],
            options={
                'verbose_name': 'subject',
                'verbose_name_plural': 'subjects',
                'db_table': 'subject',
                'ordering': ['name'],
            },
        ),
    ]
