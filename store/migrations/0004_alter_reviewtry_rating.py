# Generated by Django 5.0 on 2024-01-05 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_reviewtry_customer_alter_reviewtry_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewtry',
            name='rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
