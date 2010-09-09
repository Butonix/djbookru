from decorators import render_to
from examples.models import Category, Example
from django.shortcuts import get_object_or_404

@render_to('examples/index.html')
def index(request):
    return {
        'categories': Category.objects.all()
    }

@render_to('examples/category.html')    
def category(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    return {
        'category': obj
    }

@render_to('examples/detail.html')      
def detail(request, pk):
    return {
        'obj': get_object_or_404(Example, pk=pk)
    }