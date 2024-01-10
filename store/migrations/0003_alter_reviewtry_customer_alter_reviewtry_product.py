# Generated by Django 5.0 on 2024-01-05 02:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_reviewtry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewtry',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
        migrations.AlterField(
            model_name='reviewtry',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
