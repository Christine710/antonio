from django.views import generic
from .models import Product


class IndexView(generic.ListView):
    template_name = 'market/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name = 'market/detail.html'
