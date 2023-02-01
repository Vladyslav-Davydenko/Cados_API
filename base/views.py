from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Advocate
from .serializers import AdvocateSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {"GET":"advocates"},
        {"GET":"advocates/<str:username>"}
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def advocate_list(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(
            Q(username__icontains=query) |
            Q(bio__icontains=query)
        )
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        advocate = Advocate.objects.create(
        username = request.data["username"],
        bio = request.data["bio"]
        )
        serializer = AdvocateSerializer(advocate)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def advocate_details(request, username):
    advocate = Advocate.objects.get(username=username)

    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        advocate.username = request.data["username"]
        advocate.bio = request.data["bio"]

        advocate.save()
        serializer = AdvocateSerializer(advocate, many = False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        advocate.delete()
        return Response("User was deleted")