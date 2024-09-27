from django.db import models
from organisations.models import Organisation

# Create your models here.


class UnsignedContract(models.Model):
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, blank=False, null=False
    )
    contract_name = models.CharField(max_length=255, blank=False, null=False)
    contract_type = models.CharField(max_length=255, blank=True, null=True)
    contract_attachment_file = models.FileField(
        upload_to="unsigned_contracts/", blank=True, null=True
    )
    contract_upload_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )

    def __str__(self):
        return f"{self.contract_name}"


class SignedContract(models.Model):
    unsigned_contract = models.ForeignKey(
        UnsignedContract, on_delete=models.CASCADE, blank=False, null=False
    )
    signee_first_name = models.CharField(max_length=255, blank=False, null=False)
    signee_last_name = models.CharField(max_length=255, blank=False, null=False)
    signed_contract_attachment_file = models.FileField(
        upload_to="signed_contracts/", blank=False, null=False
    )
    contract_signed_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )

    def __str__(self):
        return f"{self.signee_first_name} {self.signee_last_name}"
