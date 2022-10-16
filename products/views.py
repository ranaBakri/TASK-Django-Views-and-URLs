from http.client import HTTPResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def get_home(request):

    return HTTPResponse("<h>Welcome to our site</h>")


def get_product(request, product_id):
    products = Product.objects.get(id=product_id)
    return HTTPResponse(
        f"""
    <p>{product.id}</p>
    <h1>{product.name}</h1>
    <p>{product.price}</p>
    """
    )
