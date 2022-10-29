from http.client import HTTPResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def get_home(request):

    return HTTPResponse("<h>Welcome to our site</h>")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
        }
    }

    return render(request, "product-detail.html", context)


def get_products(request):
    products = Product.objects.all()
    _products = []
    for product in products:
        _products.append(
            {
                "id": product.id,
                "name": product.name,
                "price": product.price,
            }
        )
    context = {"products": _products}

    return render(request, "product-list.html", context)
