from rest_framework import serializers
from .models import SignedContract, UnsignedContract
from accounts.serializers import MinimizedUserSerializer
from organisations.serializers import MinimizedOrganisationSerializer


class UnsignedContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnsignedContract
        exclude = ["contract_upload_date"]

        extra_kwargs = {
            "organisation": {"required": True},
            "contract_name": {"required": True},
            "contract_attachment_file": {"required": True},
        }


class RetrieveUnsignedContractSerializer(serializers.ModelSerializer):
    organisation = MinimizedOrganisationSerializer()

    class Meta:
        model = UnsignedContract
        fields = "__all__"


class UpdateUnsignedContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnsignedContract
        fields = "__all__"


class MinimizedUnsignedContract(serializers.ModelSerializer):

    class Meta:
        model = UnsignedContract
        fields = ["id", "organisation", "contract_name"]


class SignedContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignedContract
        exclude = ["contract_signed_date"]

        extra_kwargs = {
            "unsigned_contract": {"required": True},
            "signee_first_name": {"required": True},
            "signee_last_name": {"required": True},
            "signed_contract_attachment_file": {"required": True},
        }


class RetrieveSignedContractSerializer(serializers.ModelSerializer):
    unsigned_contract = MinimizedUnsignedContract()

    class Meta:
        model = SignedContract
        fields = "__all__"


class UpdateSignedContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = SignedContract
        fields = "__all__"
