# Generated by Django 4.2.6 on 2024-02-15 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0042_alter_activitycodes_trantype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Days', 'In Days'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('IR Date', 'IR Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Publication Date', 'PublicationDate'), ('RunDate', 'RunDate'), ('PCT Filing Date', 'PCT Filing Date'), ('Priority Date', 'Priority Date'), ('Renewal Date', 'Renewal Date'), ('Registration Date', 'RegistrationDate'), ('Application Date', 'Application Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Document Date', 'Document Date'), ('Document Receipt Date', 'Document Receipt Date'), ('OA Mailing Date', 'OA Mailing Date')], max_length=30, null=True),
        ),
    ]
