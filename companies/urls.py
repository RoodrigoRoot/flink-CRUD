from django.urls import path
from .views import CompanyCreateAPIView, CompanyRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("api/v1/companies/", CompanyCreateAPIView.as_view(), name="create_company"),
    path("api/v1/companies/<str:symbol>/", CompanyRetrieveUpdateDestroyAPIView.as_view(), name="rud_company"),
    
]
