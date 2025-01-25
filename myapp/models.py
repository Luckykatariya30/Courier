import uuid
from django.db import models
# Create your models here.

class Courier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    courierOutType = models.BooleanField(default=True)
    date = models.DateField()
    createdDate = models.DateField(null=True, blank=True)
    lrUpdateDate = models.DateField()
    voucherCodeId = models.UUIDField(default=uuid.uuid4, editable=False)
    voucherCode = models.CharField(max_length=100)
    voucherNo = models.IntegerField()
    partyId = models.UUIDField(default=uuid.uuid4, editable=False)
    partyName = models.CharField(max_length=255)
    partyGroupCode = models.CharField(max_length=100)
    courierNameId = models.UUIDField(null=True, blank=True)
    courierName = models.CharField(max_length=255, null=True, blank=True)
    courierNameAsRemark = models.CharField(max_length=255, null=True, blank=True)
    saleBillId = models.UUIDField(default=uuid.uuid4, editable=False)
    saleBillNo = models.CharField(max_length=100)
    saleType = models.CharField(max_length=100)
    courierNo = models.CharField(max_length=100)
    courierNoDate = models.DateField()
    documentType = models.CharField(max_length=100)
    courierCharges = models.FloatField(null=True, blank=True)
    paymentStatus = models.BooleanField(default=False)
    stationName = models.CharField(max_length=255)
    stateName = models.CharField(max_length=255)
    pinCode = models.CharField(max_length=10)
    remark = models.TextField(null=True, blank=True)
    createdBy = models.CharField(max_length=255)
    updatedBy = models.CharField(max_length=255, null=True, blank=True)
    deletedStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.partyName
