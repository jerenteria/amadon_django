from django.shortcuts import render, redirect
from .models import * 


def home_reroute(request):
    return redirect('/amadon')

def amadon(request):
    context={
        'all_products':Product.objects.all(),
        'quantity':[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, "amadon.html", context)

def process_purchase(request, product_id):
    if request.method=='POST':
        product=Product.objects.get(id=product_id)
        new_order=Order.objects.create(quantity=int(request.POST['quantity']), total_charge=int(request.POST['quantity'])*product.price)
        new_order.items_ordered.add(product)
        return redirect('/amadon/checkout')
    return redirect('/amadon')

def success(request):
    all_orders=Order.objects.all()
    total_spent=0
    for order in all_orders:
        total_spent+=order.total_charge
    context={
        'last_order':Order.objects.last(),
        'all_orders':all_orders,
        'grand_total':total_spent,
    }
    return render(request, "success.html", context)