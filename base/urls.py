from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #Advocates
    path("", views.getRoutes, name="get-Routes"),
    path("advocates/", views.advocate_list, name="advocates"),
    path("advocates/<str:username>/", views.AdvocateDetail.as_view(), name="advocate_details"),

    #Company
    path("companies/", views.company_list, name="company-list"),

    #Tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
