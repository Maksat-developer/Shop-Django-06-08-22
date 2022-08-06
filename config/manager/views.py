from django.shortcuts import render

def index(request):
    return render(request, template_name='manager/index.html')


def shop(request):
    return render(request, template_name='manager/shop.html')


def detail(request):
    return render(request, template_name='manager/detail.html')


def checkout(request):
    return render(request, template_name='manager/checkout.html')


def contact(request):
    return render(request, template_name='manager/contact.html')


    
def cart(request):
    return render(request, template_name='manager/cart.html')














