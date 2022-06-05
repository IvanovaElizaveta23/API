from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Product, Category


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')


def test(request):
    if 'query' in request.GET:
        q = request.GET['query']
        product=Product.objects.filter(title__icontains=q)
    else:
        product=Product.objects.all()
    return render(request, 'main/test.html', {'product':product})

class Index(TemplateView):
    template_name = "about.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context



