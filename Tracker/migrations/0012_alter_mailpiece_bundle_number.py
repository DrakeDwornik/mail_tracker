# Generated by Django 4.0 on 2022-01-03 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0011_alter_mailpiece_anticipateddeliverydate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailpiece',
            name='bundle_number',
            field=models.IntegerField(null=True),
        ),
    ]
