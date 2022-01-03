from django.db import models
from django.db.models.functions import Substr


class Mailing(models.Model):
    customer = models.CharField(max_length=100)
    mailing_name = models.CharField(max_length=100)
    mailing_dropoff_date = models.DateField()
    mailing_type_description = models.CharField(max_length=50)
    job_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.customer}"


class LiveMailpieceManager(models.Manager):
    def get_queryset(self):
        return super.get_queryset().filter()


class ZipMailpieceManager(models.Manager):
    def get_queryset(self):
        return super(ZipMailpieceManager, self).get_queryset().annotate(
            zip3=Substr('zip', 1, 3)).annotate(zip5=Substr('zip', 1, 5))


class Mailpiece(models.Model):
    mailing_id = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    pieceId = models.UUIDField(editable=False, null=True)
    edocMailingGroupId = models.CharField(max_length=50, null=True)
    idTag = models.CharField(max_length=50, null=True)
    imb = models.CharField(max_length=31, unique=True)
    mailClassDescription = models.CharField(max_length=50)
    imbMid = models.CharField(max_length=9, null=True)
    imbRoutingCode = models.CharField(max_length=11, null=True)
    imbTrackingCode = models.CharField(max_length=20, null=True)
    expectedDeliveryDate = models.DateField(null=True)
    startTheClockDate = models.DateField(null=True)
    imbSerialNumber = models.CharField(max_length=11)
    imbStid = models.CharField(max_length=3, null=True)
    anticipatedDeliveryDate = models.DateField(null=True)
    predictedDeliveryDate = models.DateField(null=True)
    routingCodeImbMatchingPortion = models.CharField(max_length=11, null=True)
    edocSubmitterCrid = models.CharField(max_length=15, null=True)
    edocJobId = models.CharField(max_length=50, null=True)
    recipient = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=50, null=True)
    address1 = models.CharField(max_length=150, null=True)
    address2 = models.CharField(max_length=150, null=True)
    address_extra = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    state = models.CharField(max_length=2, null=True)
    zip = models.CharField(max_length=10, null=True)
    record_number = models.IntegerField(null=True)
    oel = models.CharField(max_length=50, null=True)
    sort_order = models.IntegerField(null=True)
    bundle_number = models.IntegerField(null=True)
    container_number = models.IntegerField(null=True)
    manifest_key = models.CharField(max_length=25, null=True)

    class Meta:
        indexes = [models.Index(fields=['imb', ]), ]

    objects = ZipMailpieceManager()
    live_objects = LiveMailpieceManager()

    def __str__(self):
        return f"{self.imb}"


class Files(models.Model):
    mailing_id = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    mailing_list = models.FileField(upload_to='cars')


class Scan(models.Model):
    piece_id = models.ForeignKey(Mailpiece, on_delete=models.CASCADE)
    scanLocaleKey = models.CharField(max_length=10, null=True)
    machineName = models.CharField(max_length=10, null=True)
    scanFacilityCity = models.CharField(max_length=100, null=True)
    scanFacilityState = models.CharField(max_length=2, null=True)
    scannerType = models.CharField(max_length=50, null=True)
    scanEventCode = models.IntegerField(null=True)
    scanDatetime = models.DateTimeField(null=True)
    handlingEventTypeDescription = models.CharField(max_length=25, null=True)
    scanFacilityZip = models.CharField(max_length=9, null=True)
    machineId = models.CharField(max_length=10, null=True)
    handlingEventType = models.CharField(max_length=10, null=True)
    scanFacilityName = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.imb_numeric}: {self.scanDatetime}"

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
