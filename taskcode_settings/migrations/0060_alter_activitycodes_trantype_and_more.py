# Generated by Django 4.2.6 on 2024-03-05 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0059_alter_duecode_fieldbsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Days', 'In Days'), ('In Months', 'In Months')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('PCT Filing Date', 'PCT Filing Date'), ('IR Date', 'IR Date'), ('Application Date', 'Application Date'), ('Renewal Date', 'Renewal Date'), ('OA Mailing Date', 'OA Mailing Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Registration Date', 'RegistrationDate'), ('Priority Date', 'Priority Date'), ('Document Date', 'Document Date'), ('Publication Date', 'PublicationDate'), ('Document Receipt Date', 'Document Receipt Date'), ('IR Renewal Date', 'IR Renewal Date'), ('RunDate', 'RunDate')], max_length=30, null=True),
        ),
    ]
