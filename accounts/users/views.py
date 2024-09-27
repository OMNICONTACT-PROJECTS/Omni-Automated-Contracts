from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.generics import (
    RetrieveDestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    GenericAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import User
from .serializers import (
    UserProfPicSerializer,
    UserProfPicRetrieveSerializer,
)
from accounts.serializers import RetrieveMinimizedUserSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from organisations.models import Organisation
from ..serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings


class UserCreateView(GenericAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:

            if serializer.is_valid():
                saved_user = serializer.save()
                data = {
                    "message": "Administrator created successfully",
                    "data": serializer.data,
                }
                saved_user.account_status = "ACTIVE"
                saved_user.role = "ADMIN"
                saved_user.is_superuser = False
                saved_user.is_staff = True
                saved_user.is_active = True
                new_username = f"{saved_user.username}AD"
                saved_user.username = new_username
                saved_user.set_password("omni-admin-123")
                saved_user.save()

                first_name = serializer.validated_data["first_name"].upper()
                last_name = serializer.validated_data["last_name"].upper()
                # username = serializer.validated_data['username']
                email = serializer.validated_data["email"]
                full_name = f"{first_name } { last_name}"
                password = "omni-admin-123"

                this_instance = User.objects.get(pk=serializer.data["id"])
                username = this_instance.username
                role = this_instance.role

                email_subject = f"Welcome to OMNI AUTOMATED CONTRACTS SYSTEM, Your ADMIN Account has been Created Successfully"
                email_to = email
                email_from = settings.EMAIL_HOST_USER
                email_body = (
                    f"Dear {full_name},\n\nWe are delighted to inform you that your account has been successfully created for the OMNI AUTOMATED CONTRACTS SYSTEM. "
                    f"You can now access your account using the following details:\n\n"
                    f"Username: {username}\n"
                    f"Password: {password}\n"
                    f"Email: {email}\n"
                    f"Role: {role}\n\n"
                    f"Kindly use the Username and password above to Sign in to your account. \n \n"
                    f"Please keep this information secure and do not share it with anyone. If you have any questions or need assistance, "
                    f"feel free to reach out to our support team at support@omnicontact.biz.\n\n"
                    f"Thank you for joining OMNI AUTOMATED CONTRACTS SYSTEM. We look forward to providing you with a great experience!\n\n"
                    f"Best regards,\n"
                    f"OMNICONTACT DEV\n"
                )

                send_mail(
                    email_subject,
                    email_body,
                    email_from,
                    [email_to],
                    fail_silently=True,
                )
                return Response(data, status=status.HTTP_201_CREATED)

            return Response(
                {
                    "message": "Failed to create administrator, Validation error occurred.",
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {
                    "message": "Failed to create administrator. Exception error occurred",
                    "error": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetAllUserView(ListAPIView):
    permission_classes = []
    serializer_class = RetrieveMinimizedUserSerializer
    queryset = User.objects.all()


class RetrieveDestroyUserView(RetrieveDestroyAPIView):
    permission_classes = []
    serializer_class = RetrieveMinimizedUserSerializer
    queryset = User.objects.all()


class UploadUserProfilePicView(UpdateAPIView):
    permission_classes = []
    serializer_class = UserProfPicSerializer
    queryset = User.objects.all()
    parser_classes = [MultiPartParser, FormParser]


class GetAllUsersByOrganisationId(GenericAPIView):
    permission_classes = []
    serializer_class = RetrieveMinimizedUserSerializer
    queryset = User.objects.all()

    def get(self, request, organisation_id, *args, **kwargs):
        try:
            organisation = Organisation.objects.get(pk=organisation_id)
        except Organisation.DoesNotExist:
            return Response(
                data={"error": "Organisation not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            users = User.objects.filter(organisation_id=organisation_id)
            serializer = self.serializer_class(users, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
