# Generated by Django 4.0 on 2022-01-03 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0009_alter_mailpiece_anticipateddeliverydate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailpiece',
            name='pieceIdUUID',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]
