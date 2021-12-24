from django.db import models


class Mailing(models.Model):
    customer = models.CharField(max_length=100)
    mailing_name = models.CharField(max_length=50)
    mailing_dropoff_date = models.DateField()
    mailing_type_description = models.CharField(max_length=50)


class Mailpiece(models.Model):
    mailing_id = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    pieceId = models.UUIDField(editable=False, unique=True)
    edocMailingGroupId = models.CharField(max_length=50)
    idTag = models.CharField(max_length=50)
    imb = models.CharField(max_length=31)
    mailClassDescription = models.CharField(max_length=50)
    imbMid = models.CharField(max_length=9)
    imbRoutingCode = models.CharField(max_length=11)
    imbTrackingCode = models.CharField(max_length=20)
    expectedDeliveryDate = models.DateField()
    startTheClockDate = models.DateField()
    imbSerialNumber = models.CharField(max_length=11)
    imbStid = models.CharField(max_length=3)
    anticipatedDeliveryDate = models.DateField()
    predictedDeliveryDate = models.DateField()
    routingCodeImbMatchingPortion = models.CharField(max_length=11)
    edocSubmitterCrid = models.CharField(max_length=15)
    edocJobId = models.CharField(max_length=50)
    recipient = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    address3 = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=9)


class Scan(models.Model):
    piece_id = models.ForeignKey(Mailpiece, on_delete=models.CASCADE)
    scanLocaleKey = models.CharField(max_length=10)
    machineName = models.CharField(max_length=10)
    scanFacilityCity = models.CharField(max_length=100)
    scanFacilityState = models.CharField(max_length=2)
    scannerType = models.CharField(max_length=50)
    scanEventCode = models.IntegerField
    scanDatetime = models.DateTimeField()
    handlingEventTypeDescription = models.CharField(max_length=25)
    scanFacilityZip = models.CharField(max_length=9)
    machineId = models.CharField(max_length=10)
    handlingEventType = models.CharField(max_length=10)
    scanFacilityName = models.CharField(max_length=50)

#
#
#
#
# data_message
# ----
# id PK bigint IDENTITY
# import_time dateTime default=GETUTCDATE() NULLABLE
# msgGrpId VARCHAR(50) NULLABLE
# msgSerNbr int NULLABLE
# totMsgCnt int NULLABLE
# recCnt int NULLABLE
# totRecCnt int NULLABLE


#
#
# https://app.quickdatabasediagrams.com/#/
