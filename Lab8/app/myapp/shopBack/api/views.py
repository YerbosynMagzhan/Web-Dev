
from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize

from api.models import Product, Category

def products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    
    return JsonResponse(products_json, safe=False)

def products_by_id(request, id):
    try:
        product = Product.objects.get(id=id)
        return JsonResponse(product.to_json(), safe=False)
    except Product.DoesNotExist as e:
        return JsonResponse({
            'error' : str(e)
        })

def categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def categories_by_id(request, id):
    try:
        category = Category.objects.get(id=id)
        return JsonResponse(category.to_json(), safe=False)
    except Category.DoesNotExist as e:
        return JsonResponse({
            'error' : str(e)
        })

def products_by_category(request, id):
    try:
        category = Category.objects.get(id=id)
        products = Product.objects.filter(category_id=id)
        products_json = []
        for product in products:
            product_json = product.to_json()
            product_json['category'] = category.to_json()
            products_json.append(product_json)
        
        return JsonResponse(products_json, safe=False)
    except Category.DoesNotExist as e:
        return JsonResponse({
            'error' : str(e)
        })