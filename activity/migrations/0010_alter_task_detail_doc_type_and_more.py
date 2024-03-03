# Generated by Django 4.2.6 on 2023-11-27 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0009_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Outgoing', 'Outgoing'), ('Incoming', 'Incoming'), ('Others', 'Others')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Personal', 'Personal'), ('Email', 'Email'), ('Court', 'Court'), ('IPO', 'IPO'), ('Mail', 'Mail')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='FilingDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('DocDate', models.DateField(blank=True, null=True)),
                ('DocsPDF', models.FileField(blank=True, null=True, upload_to='Documents/%Y/%m/%D/')),
                ('createdby', models.CharField(blank=True, max_length=30, null=True)),
                ('updatedby', models.CharField(blank=True, max_length=30, null=True)),
                ('datemodified', models.DateTimeField(auto_now=True)),
                ('datecreated', models.DateTimeField(auto_now_add=True)),
                ('task_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.task_detail')),
            ],
        ),
    ]
