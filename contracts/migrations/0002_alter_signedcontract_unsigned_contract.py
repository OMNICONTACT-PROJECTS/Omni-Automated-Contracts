# Generated by Django 5.1.1 on 2024-10-21 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signedcontract',
            name='unsigned_contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signed_contracts', to='contracts.unsignedcontract'),
        ),
    ]
