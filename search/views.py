from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

class SearchProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "search/views.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.filter(title__icontantains=query)
        return Product.objects.none()

# Create your views here.
