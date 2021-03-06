# Generated by Django 4.0 on 2022-01-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0019_alter_mailpiece_address1_alter_mailpiece_address2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='scanEventCode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='handlingEventType',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='handlingEventTypeDescription',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='machineId',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='machineName',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scanDatetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scanFacilityCity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scanFacilityName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scanFacilityState',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scanFacilityZip',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scanLocaleKey',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scannerType',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
