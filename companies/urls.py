from django.urls import path
from .views import CompanyListCreateAPIView, CompanyRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("api/v1/companies/", CompanyListCreateAPIView.as_view(), name="create_company"),
    path("api/v1/companies/<uuid:auto_id>/", CompanyRetrieveUpdateDestroyAPIView.as_view(), name="rud_company"),
    
]
