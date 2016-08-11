from django.shortcuts import render
from django.views import generic
from .models import Product
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def market(request):
    return render(request, 'market/index.html')

class IndexView(generic.ListView):
    template_name = 'market/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name = 'market/detail.html'

