from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserCreateView.as_view(), name="user_create"),
    path(
        "get-by-organisation-id/<int:organisation_id>/",
        views.GetAllUsersByOrganisationId.as_view(),
    ),
    path("get-all/", views.GetAllUserView.as_view()),
    path("<int:pk>/", views.RetrieveDestroyUserView.as_view()),
    path(
        "upload-user-profile-picture/<int:pk>/",
        views.UploadUserProfilePicView.as_view(),
    ),
]
