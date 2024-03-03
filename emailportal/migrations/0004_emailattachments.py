# Generated by Django 4.2.6 on 2024-02-19 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emailportal', '0003_emails_matter'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAttachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailattachment', models.FileField(blank=True, null=True, upload_to='EmailAttachments/%Y/%m/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('edited_at', models.DateTimeField(auto_now=True, null=True)),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emailportal.emails')),
            ],
        ),
    ]