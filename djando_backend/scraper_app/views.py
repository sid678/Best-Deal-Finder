from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from . import amazon

# Create your views here.
def home(request):
    if request.method == 'POST':
        product=request.POST.get('product')
        request.session['query']=product
        return HttpResponseRedirect(reverse('show_deal'))
    return render(request, 'scraper_app/index.html')

def show_deal(request, productName):
    # query = request.session.get('query', None)
    items = amazon.scrape(productName)
    print(items[0])
    # return render(request, 'scraper_app/show_deal.html', {'items':items})
    return JsonResponse(items, safe=False)