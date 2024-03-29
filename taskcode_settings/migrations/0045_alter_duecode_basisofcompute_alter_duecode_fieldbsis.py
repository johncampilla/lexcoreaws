# Generated by Django 4.2.6 on 2024-02-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0044_alter_duecode_basisofcompute_alter_duecode_fieldbsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Days', 'In Days'), ('In Months', 'In Months')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Renewal Date', 'Renewal Date'), ('RunDate', 'RunDate'), ('Document Receipt Date', 'Document Receipt Date'), ('Application Date', 'Application Date'), ('Registration Date', 'RegistrationDate'), ('IR Date', 'IR Date'), ('PCT Filing Date', 'PCT Filing Date'), ('PCT Publication Date', 'PCT Publication Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Document Date', 'Document Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Publication Date', 'PublicationDate'), ('Priority Date', 'Priority Date')], max_length=30, null=True),
        ),
    ]
