# Generated by Django 4.2.6 on 2024-01-23 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_lookup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitygroup',
            name='case_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reference_lookup.casetype'),
        ),
    ]
