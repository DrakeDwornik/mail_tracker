# Generated by Django 4.0 on 2022-01-03 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0007_rename_pieceid_mailpiece_pieceiduuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailpiece',
            name='pieceIdUUID',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]