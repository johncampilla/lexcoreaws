# Generated by Django 4.2.6 on 2024-03-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_client_data_country_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_data',
            name='category',
            field=models.CharField(blank=True, choices=[('Corporate', 'Corporate/Company'), ('Individual', 'Individual'), ('School', 'School'), ('Government', 'Government')], max_length=20, null=True),
        ),
    ]
