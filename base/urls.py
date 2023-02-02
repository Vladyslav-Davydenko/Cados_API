from django.urls import path
from . import views

urlpatterns = [
    #Advocates
    path("", views.getRoutes, name="get-Routes"),
    path("advocates/", views.advocate_list, name="advocates"),
    path("advocates/<str:username>/", views.AdvocateDetail.as_view(), name="advocate_details"),

    #Company
    path("companies/", views.company_list, name="company-list"),
]
