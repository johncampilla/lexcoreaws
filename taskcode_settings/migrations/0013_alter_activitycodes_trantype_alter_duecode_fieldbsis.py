# Generated by Django 4.2.6 on 2023-11-29 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0012_alter_duecode_basisofcompute_alter_duecode_fieldbsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('BILLABLE', 'BILLABLE'), ('MAILSIN', 'MAILSIN')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Document Date', 'Document Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Publication Date', 'PublicationDate'), ('Renewal Date', 'Renewal Date'), ('Priority Date', 'Priority Date'), ('Registration Date', 'RegistrationDate'), ('Document Receipt Date', 'Document Receipt Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Application Date', 'Application Date'), ('OA Mailing Date', 'OA Mailing Date')], max_length=30, null=True),
        ),
    ]
