# Generated by Django 4.2.6 on 2023-11-27 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matter', '0002_caseevidence'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_description', models.TextField(blank=True, null=True)),
                ('case_theory', models.TextField(blank=True, null=True)),
                ('matter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matter.matters')),
            ],
            options={
                'verbose_name_plural': 'Case Description/Theory',
            },
        ),
    ]
