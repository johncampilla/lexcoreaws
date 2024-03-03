# Generated by Django 4.2.6 on 2023-11-13 07:22

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Corporate', 'Corporate/Company'), ('Individual', 'Individual'), ('School', 'School'), ('Government', 'Government')], max_length=20)),
                ('address', models.CharField(max_length=250, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('zip_code', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=200, null=True)),
                ('landline', models.CharField(blank=True, max_length=100)),
                ('entity_type', models.CharField(blank=True, choices=[('Big Entity', 'Big Entity'), ('Small Entity', 'Small Entity')], max_length=20, null=True)),
                ('date_acquired', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Dormant', 'Dormant'), ('Delinquent', ' Delinquent')], default='Active', max_length=15)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('referredby', models.CharField(blank=True, max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('local_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='NatureOfBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Nature Of Business',
            },
        ),
        migrations.CreateModel(
            name='Contact_Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.client_data')),
            ],
            options={
                'verbose_name_plural': "Client's Contact Persons",
            },
        ),
        migrations.AddField(
            model_name='client_data',
            name='billing_currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.currency'),
        ),
        migrations.AddField(
            model_name='client_data',
            name='industry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.natureofbusiness'),
        ),
        migrations.CreateModel(
            name='Client_Bill_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_to', models.CharField(blank=True, max_length=100)),
                ('billing_address', models.CharField(blank=True, max_length=200)),
                ('billing_attention', models.CharField(blank=True, max_length=60)),
                ('position', models.CharField(blank=True, max_length=60)),
                ('billing_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.currency')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client.client_data')),
            ],
            options={
                'verbose_name_plural': 'Clients Billing Parameters',
            },
        ),
    ]