from django.shortcuts import render
from django.http import HttpResponse
from .models import BasicResource, CreatedItem
# Create your views here.
def index(request):
    c_items = CreatedItem.objects.order_by('-name')
    b_items = BasicResource.objects.order_by('-name')
    output = ', '.join([i.name for i in c_items])
    return HttpResponse(output)

def detail(request, item_id):
    response = "You're looking at item %s." % item_id
    return HttpResponse(response % item_id)

