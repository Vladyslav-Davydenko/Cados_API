from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="get-Routes"),
    path("advocates/", views.advocate_list, name="advocates"),
    path("advocates/<str:username>/", views.advocate_details, name="advocate_details")
]
