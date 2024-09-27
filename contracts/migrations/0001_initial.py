# Generated by Django 5.1.1 on 2024-09-27 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnsignedContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_name', models.CharField(max_length=255)),
                ('contract_type', models.CharField(blank=True, max_length=255, null=True)),
                ('contract_attachment_file', models.FileField(blank=True, null=True, upload_to='unsigned_contracts/')),
                ('contract_upload_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisations.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='SignedContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signee_first_name', models.CharField(max_length=255)),
                ('signee_last_name', models.CharField(max_length=255)),
                ('signed_contract_attachment_file', models.FileField(upload_to='signed_contracts/')),
                ('contract_signed_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('unsigned_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.unsignedcontract')),
            ],
        ),
    ]
