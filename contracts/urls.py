from django.urls import path
from . import views

urlpatterns = [
    path("unsigned-contracts/", views.UnsignedContractCreateView.as_view()),
    path(
        "unsigned-contracts/<int:pk>/",
        views.RetrieveDestroyUnsignedContractView.as_view(),
    ),
    path("unsigned-contracts/get-all/", views.GetAllUnsignedContractsView.as_view()),
    path(
        "unsigned-contracts/get-all-by-organisation-id/<int:organisation_id>/",
        views.GetAllUnsignedContractsByOrganisationId.as_view(),
    ),
    path(
        "unsigned-contracts/update/<int:pk>/",
        views.UpdateUnsignedContractView.as_view(),
    ),
    path("signed-contracts/", views.SignedContractCreateView.as_view()),
    path(
        "signed-contracts/<int:pk>/", views.RetrieveDestroySignedContractView.as_view()
    ),
    path("signed-contracts/get-all/", views.GetAllSignedContractsView.as_view()),
    path(
        "signed-contracts/get-all-by-organisation-id/<int:organisation_id>/",
        views.GetAllSignedContractsByOrganisationId.as_view(),
    ),
    path("signed-contracts/update/<int:pk>/", views.UpdateSignedContractView.as_view()),
    path(
        "signed-contracts/get-by-unsigned-contract-id/<int:unsigned_contract_id>/",
        views.GetSignedContractsByUnsignedContractId.as_view(),
    ),
    path(
        "unsigned-contracts-with-signatures/<int:organisation_id>/",
        views.UnsignedContractsWithSignaturesListView.as_view(),
        name="unsigned-contracts-with-signatures",
    ),
    path(
        "get-all-stats-by-organisation-id/<int:organisation_id>/",
        views.ContractStatsView.as_view(),
    ),
]
