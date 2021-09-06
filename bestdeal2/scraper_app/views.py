from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from . import amazon, flipkart, snapdeal, sort_fn, ShopClues

# Create your views here.
def home(request):
    if request.method == 'POST':
        product=request.POST.get('product')
        request.session['query']=product
        return HttpResponseRedirect(reverse('show_deal'))
    return render(request, 'scraper_app/index.html')

# def show_deal(request):
#     query = request.session.get('query', None)
#     a_items = sort_fn.RankProducts(amazon.scrape(query),10)
#     f_items = sort_fn.RankProducts(flipkart.getItems(query),10)
#     s_items = sort_fn.RankProducts(snapdeal.snapdeal(query),10)
#     sc_items = sort_fn.RankProducts(ShopClues.scrape(query),10)
#     items = a_items + s_items + f_items + sc_items
#     deals = sort_fn.RankProducts(items,40,1)
#     return render(request, 'scraper_app/show_deal.html', {'deals': deals, 'a_items':a_items, 'f_items':f_items, 's_items':s_items})
def show_deal(request, productName):
    # query = request.session.get('query', None)
    a_items=amazon.scrape(productName)
    f_items=flipkart.getItems(productName)
    s_items=snapdeal.snapdeal(productName)
    sc_items=ShopClues.scrape(productName)
    items2=a_items + s_items + f_items + sc_items
    if a_items!=[]:
        a_items = sort_fn.RankProducts(a_items, 10)
    if f_items!=[]:
        f_items = sort_fn.RankProducts(f_items, 10)
    if s_items!=[]:
        s_items = sort_fn.RankProducts(s_items, 10)
    if sc_items!=[]:
        sc_items = sort_fn.RankProducts(sc_items, 10)
    items = a_items + s_items + f_items + sc_items
    deals=[]
    if items!=[]:
        deals = sort_fn.RankProducts(items,40,1)
    # return render(request, 'scraper_app/show_deal.html', {'items':items})
    return JsonResponse({'deals':deals, 'items':items}, safe=False)

def getFilteredData(request, productName, minimum, maximum):
    #request.lower_bound, request.upper_bound
    #give these to sort function with items
    minimum=float(minimum)
    maximum=float(maximum)
    a_items=amazon.scrape(productName)
    f_items=flipkart.getItems(productName)
    s_items=snapdeal.snapdeal(productName)
    sc_items=ShopClues.scrape(productName)
    items2=a_items + s_items + f_items + sc_items
    items3=[]
    for item in items2:
        if item['price_inr']!='':
            item_price = float(item['price_inr'].strip().replace(',', ''))
            if item_price>=minimum and item_price<=maximum:
                items3.append(item)

    deals=[]
    if items3!=[]:
        deals = sort_fn.RankProducts(items3,40,1)
    return JsonResponse(deals, safe=False)