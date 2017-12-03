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
            return Product.objects.filter(title__icontains=query)
        return Product.objects.none()

    def get_context_data(self,*args, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*args,**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query)
        return context
# Create your views here.
