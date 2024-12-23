from .serializers import (
    UnsignedContractSerializer,
    RetrieveUnsignedContractSerializer,
    UpdateUnsignedContractSerializer,
    SignedContractSerializer,
    RetrieveSignedContractSerializer,
    UpdateSignedContractSerializer,
)
from .models import UnsignedContract, SignedContract
from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from accounts.models import User
from organisations.models import Organisation

# Create your views here.


class UnsignedContractCreateView(GenericAPIView):
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = UnsignedContractSerializer
    queryset = UnsignedContract.objects.all()

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        try:
            if serializer.is_valid():
                serializer.save()
                data = {
                    "message": "Contract uploaded successfully",
                    "data": serializer.data,
                }
                return Response(data, status=status.HTTP_201_CREATED)

            return Response(
                {
                    "message": "Failed to upload contract, Validation error occurred.",
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return (
                Response(
                    {
                        "message": "Failed to upload contract, Exception error occurred.",
                        "error": str(e),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                ),
            )


class GetAllUnsignedContractsByOrganisationId(GenericAPIView):
    permission_classes = []
    serializer_class = RetrieveUnsignedContractSerializer
    queryset = UnsignedContract.objects.all()

    def get(self, request, organisation_id):
        try:
            Organisation.objects.get(pk=organisation_id)
        except Organisation.DoesNotExist:
            return Response(
                data={"message": "Organisation does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            contract = self.queryset.filter(organisation_id=organisation_id).order_by(
                "-contract_upload_date"
            )
            serializer = self.serializer_class(contract, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllUnsignedContractsView(ListAPIView):
    permission_classes = []
    serializer_class = RetrieveUnsignedContractSerializer
    queryset = UnsignedContract.objects.all()


class UpdateUnsignedContractView(GenericAPIView):
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = UpdateUnsignedContractSerializer
    queryset = UnsignedContract.objects.all()

    def put(self, request, pk):
        try:
            contract = self.queryset.get(pk=pk)
        except UnsignedContract.DoesNotExist:
            return Response(
                data={"error": "Contract not Found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            serializer = self.serializer_class(
                contract, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveDestroyUnsignedContractView(RetrieveDestroyAPIView):
    permission_classes = []
    serializer_class = RetrieveUnsignedContractSerializer
    queryset = UnsignedContract.objects.all()


class SignedContractCreateView(GenericAPIView):
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = SignedContractSerializer
    queryset = SignedContract.objects.all()

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        try:
            if serializer.is_valid():
                serializer.save()
                data = {
                    "message": "Contract uploaded successfully",
                    "data": serializer.data,
                }
                return Response(data, status=status.HTTP_201_CREATED)

            return Response(
                {
                    "message": "Failed to upload contract, Validation error occurred.",
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return (
                Response(
                    {
                        "message": "Failed to upload contract, Exception error occurred.",
                        "error": str(e),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                ),
            )


class GetAllSignedContractsByOrganisationId(GenericAPIView):
    permission_classes = []
    serializer_class = RetrieveSignedContractSerializer
    queryset = SignedContract.objects.all()

    def get(self, request, organisation_id):
        try:
            Organisation.objects.get(pk=organisation_id)
        except Organisation.DoesNotExist:
            return Response(
                data={"message": "Organisation does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            contract = self.queryset.filter(
                unsigned_contract__organisation_id=organisation_id
            ).order_by("-contract_signed_date")
            serializer = self.serializer_class(contract, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllSignedContractsView(ListAPIView):
    permission_classes = []
    serializer_class = RetrieveSignedContractSerializer
    queryset = SignedContract.objects.all()


class UpdateSignedContractView(GenericAPIView):
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = UpdateSignedContractSerializer
    queryset = SignedContract.objects.all()

    def put(self, request, pk):
        try:
            contract = self.queryset.get(pk=pk)
        except SignedContract.DoesNotExist:
            return Response(
                data={"error": "Contract not Found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            serializer = self.serializer_class(
                contract, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveDestroySignedContractView(RetrieveDestroyAPIView):
    permission_classes = []
    serializer_class = RetrieveSignedContractSerializer
    queryset = SignedContract.objects.all()


class GetSignedContractsByUnsignedContractId(GenericAPIView):
    permission_classes = []
    serializer_class = RetrieveSignedContractSerializer
    queryset = SignedContract.objects.all()

    def get(self, request, unsigned_contract_id):
        try:
            UnsignedContract.objects.get(pk=unsigned_contract_id)
        except UnsignedContract.DoesNotExist:
            return Response(
                data={"message": "Unsigned Contract does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            contracts = self.queryset.filter(
                unsigned_contract_id=unsigned_contract_id
            ).order_by("-contract_signed_date")
            serializer = self.serializer_class(contracts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class UnsignedContractsWithSignaturesListView(GenericAPIView):
    permission_classes = []
    serializer_class = RetrieveUnsignedContractSerializer
    queryset = UnsignedContract.objects.all()

    def get(self, request, organisation_id):
        try:
            Organisation.objects.get(pk=organisation_id)
        except Organisation.DoesNotExist:
            return Response(
                data={"message": "Organisation does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            contracts = (
                self.queryset.filter(
                    signed_contracts__isnull=False, organisation_id=organisation_id
                )
                .order_by("-contract_upload_date")
                .distinct()
            )
            serializer = self.serializer_class(contracts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class ContractStatsView(GenericAPIView):
    permission_classes = []
    serializer_class = RetrieveUnsignedContractSerializer
    queryset = UnsignedContract.objects.all()

    def get(self, request, organisation_id):
        try:
            Organisation.objects.get(pk=organisation_id)
        except Organisation.DoesNotExist:
            return Response(
                data={"message": "Organisation does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

        signed_contracts = (
            UnsignedContract.objects.filter(
                signed_contracts__isnull=False, organisation_id=organisation_id
            )
            .order_by("-contract_upload_date")
            .distinct()
        ).count()

        all_contracts = self.queryset.filter(organisation_id=organisation_id).count()

        total_signatures = SignedContract.objects.filter(
            unsigned_contract__organisation_id=organisation_id
        ).count()

        # Calculate percentages
        if all_contracts > 0:
            signed_percentage = (signed_contracts / all_contracts) * 100
            unsigned_percentage = 100 - signed_percentage
        else:
            signed_percentage = 0
            unsigned_percentage = 0

        stats = {
            "total_signed_contracts": signed_contracts,
            "total_contracts": all_contracts,
            "total_unsigned_contracts": (all_contracts - signed_contracts),
            "total_signatures": total_signatures,
            "signed_percentage": round(signed_percentage, 2),
            "unsigned_percentage": round(unsigned_percentage, 2),
        }

        return Response(stats, status=status.HTTP_200_OK)
