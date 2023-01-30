from django.shortcuts import render
from django.http import JsonResponse

def getRoutes(request):
    data = ["/advocates", "advocates/:username"]
    return JsonResponse(data, safe=False)

def advocate_list(request):
    data = ["Vilsivul", "The_RealSanya", "Bob"]
    return JsonResponse(data, safe=False)


def advocate_details(request, username):
    data = username
    return JsonResponse(data, safe=False)
