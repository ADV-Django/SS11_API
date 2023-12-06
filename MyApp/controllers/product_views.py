import datetime

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from MyApp.serailizers.CategorySerializer import CategorySerializer
from MyApp.models import Category, Product
from MyApp.serailizers.ProductSerializer import ProductSerializer


# Create your views here.
@api_view(["GET"])
def index(request):
    product=Product.objects.all()
    serializer=ProductSerializer(product,many=True)
    return Response(serializer.data)
@api_view(["POST"])
def store(request):
    product=Product()
    product.name=request.data["name"]
    product.barcode = request.data["barcode"]
    product.sellPrice = request.data["sellPrice"]
    product.category_id= request.data["category"]
    product.createBy_id=request.data["createBy"]
    if len(request.data["photo"])>0:
        product.photo = request.data["photo"]
        product.save()
        return Response({"message":"Product created"},status=status.HTTP_201_CREATED)
    else:
        product.photo =""
        product.save()
        return Response({"message": "Product created"}, status=status.HTTP_201_CREATED)
@api_view(["GET"])
def findById(request,id):
    try:
        product=Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({"message": "not found id:" + id})
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(["POST"])
def findByName(request):
    try:
        product=Product()
        product.name=request.data["name"]
        product1=Product.objects.filter(name=product.name)
        if product1.count()==0:
            return Response({"message":"search not found:"+product.name})
        serializer = CategorySerializer(product1,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"Error":""+str(ex)},status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET","DELETE"])
def deleteById(request,id):
    try:
        product=Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({"message":"not found id:"+id})
    if product.photo:
        product.photo.delete()
        product.delete()
    else:
        product.delete()
    return Response({"message":"Product deleted"},status=status.HTTP_200_OK)
@api_view(["GET","PUT"])
def updateById(request,id):
    try:
        product=Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({"message":"not found:"+id})

    product.name = request.data["name"]
    product.barcode = request.data["barcode"]
    product.sellPrice = request.data["sellPrice"]
    product.category_id = request.data["category"]
    product.updateBy_id = request.data["updateBy"]
    product.updateAt=datetime.datetime.now()
    if product.photo:
        if len(request.data['photo'])>0:
            product.photo.delete()
            product.photo=request.data["photo"]
            product.save()
        else:
            product.save()
    else:
        if len(request.data['photo'])>0:
            product.photo=request.data["photo"]
            product.save()
        else:
            product.photo=""
            product.save()
    return Response({"message":"Product updated"},status=status.HTTP_200_OK)

