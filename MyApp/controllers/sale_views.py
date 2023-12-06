import datetime

from django.db import transaction
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from MyApp.serailizers.CategorySerializer import CategorySerializer
from MyApp.models import Category, Product, Sale, SaleDetail
from MyApp.serailizers.ProductSerializer import ProductSerializer


# Create your views here.
@api_view(["POST"])
def commit_data(request):
    try:
        with transaction.atomic():
            sale=Sale()
            sale.totalAmount=request.data["totalAmount"]
            sale.createBy_id=request.data["createBy"]
            sale.save()
            # add data to table saleDetail
            saleId=Sale.objects.last()
            for i in range(len(request.data["sale"])):
                saleDetail=SaleDetail()
                saleDetail.sale_id=saleId.id
                saleDetail.product_id = request.data["sale"][i]["product"]
                saleDetail.qty=request.data["sale"][i]["qty"]
                saleDetail.price = request.data["sale"][i]["price"]
                saleDetail.amount=saleDetail.qty * saleDetail.price
                saleDetail.save()
                #----------------------
                product=Product.objects.get(pk=saleDetail.product_id)
                if product:
                    product.qtyInstock=product.qtyInstock-saleDetail.qty
                    product.save()
        transaction.commit()
        return Response({"message":"data committed"})
    except Exception as ex:
        return  Response({"Error:"+str(ex)})