from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.filter()
    template_name = "products/details.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("NotFound")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Tor matha")

        return instance


class ProductDetailsView(DetailView):
    queryset = Product.objects.filter()
    template_name = "products/details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailsView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product does not exist")
        return instance

# Create your views here.
