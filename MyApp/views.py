import datetime

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from MyApp.CategorySerializer import CategorySerializer
from MyApp.models import Category
# Create your views here.
@api_view(["GET"])
def index(request):
    category=Category.objects.all()
    serializer=CategorySerializer(category,many=True)
    return Response(serializer.data)
@api_view(["POST"])
def store(request):
    category=Category()
    category.name=request.data["name"]
    category.createBy_id=request.data["createBy"]
    data={
        "name":category.name,
        "createBy":category.createBy_id
    }
    serializer=CategorySerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message":"Category Created"},status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,exception=True)
@api_view(["GET"])
def findById(request,id):
    try:
        category=Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response({"message": "not found id:" + id})
    serializer = CategorySerializer(category)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(["POST"])
def findByName(request):
    try:
        category=Category()
        category.name=request.data["name"]
        category1=Category.objects.filter(name=category.name)
        if category1.count()==0:
            return Response({"message":"search not found:"+category.name})
        serializer = CategorySerializer(category1,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"Error":""+str(ex)},status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET","DELETE"])
def deleteById(request,id):
    try:
        category=Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response({"message":"not found id:"+id})
    category.delete()
    return Response({"message":"Category deleted"},status=status.HTTP_200_OK)
@api_view(["GET","PUT"])
def updateById(request,id):
    try:
        category=Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response({"message":"not found id:"+id})
    category.name=request.data["name"]
    category.updateBy_id=request.data["updateBy"]
    category.updateAt=datetime.datetime.now()
    data={
        "name":category.name,
        "updateBy":category.updateBy_id,
        "updateAt":category.updateAt
    }
    serializer=CategorySerializer(category,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Category updated"})
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

