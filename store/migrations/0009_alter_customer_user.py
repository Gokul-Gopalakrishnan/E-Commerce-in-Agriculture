# Generated by Django 3.2.5 on 2021-10-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
