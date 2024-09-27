from django.db import models
from django.contrib.auth.models import AbstractUser
from organisations.models import Organisation


class User(AbstractUser):
    # exclude fields from AbstractUser
    date_joined = None
    last_login = None
    email = None

    GENDER = (
    ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
    )
    ROLE = (
        ("SUPERUSER", "SUPERUSER"),
        ("ADMIN", "ADMIN"),
    )
    ACCOUNT_STATUS = (
        ("ACTIVE", "ACTIVE"),
        ("INACTIVE", "INACTIVE"),
    )
    organisation = models.ForeignKey(
        Organisation, blank=True, null=True, on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    role = models.CharField(max_length=25, blank=True, null=True, choices=ROLE)
    gender = models.CharField(max_length=15, blank=True, null=True, choices=GENDER)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    job_title = models.CharField(max_length=150, blank=True, null=True)
    current_location = models.CharField(max_length=155, blank=True, null=True)
    account_status = models.CharField(
        max_length=150, blank=True, null=True, choices=ACCOUNT_STATUS
    )
    account_creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="user_profile_pictures", blank=True, null=True
    )

    date_created = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
