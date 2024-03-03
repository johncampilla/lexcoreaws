# Generated by Django 4.2.6 on 2024-02-17 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0049_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Others', 'Others'), ('Outgoing', 'Outgoing'), ('Incoming', 'Incoming')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Mail', 'Mail'), ('IPO', 'IPO'), ('Personal', 'Personal'), ('Court', 'Court'), ('Email', 'Email')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
    ]