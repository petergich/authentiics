from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import shoes
from .forms import MyModelForm
import json
def home(request):
    if 'search' in request.GET:
         search_text = request.GET.get('search', '').lower()
         if search_text=="":
             my_shoes=shoes.objects.all()
             return render(request,'index.html',{"items":my_shoes})
         else:
              my_shoes = shoes.objects.filter(name__icontains=search_text)
              if len(my_shoes)==1:
                  my_shoe=shoes.objects.get(name__icontains=search_text)
                  return redirect('myapp:item_detail', item_id=my_shoe.id)
              else:
                   return render(request,'index.html',{"items":my_shoes})
    else:

        my_shoes=shoes.objects.all()
        return render(request,'index.html',{"items":my_shoes})
    
def item(request,item_id):
    item=shoes.objects.get(id=item_id)
    print(item)
    return render(request,'items.html',{"shoe":item})

def get_filtered_options(request):
    search_text = request.GET.get('search', '').lower()
    options = shoes.objects.filter(name__icontains=search_text)
    values=[]
    for val in options:
        values.append(val.name)
    return JsonResponse(values, safe=False)

# Create your views here.
