# Generated by Django 4.0 on 2022-01-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0016_alter_mailpiece_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='mailing_name',
            field=models.CharField(max_length=100),
        ),
    ]