from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context


class ProductDetailsView(DetailView):
    queryset = Product.objects.filter()
    template_name = "products/details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailsView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

# Create your views here.
