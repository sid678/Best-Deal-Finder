import numpy as np
import operator
from operator import itemgetter

def RankProducts(products_data, items_to_take, final_pass=False):
    wt_price = -1.0
    wt_avgr = 1.0
    wt_numr = 1.0
   
    amb = []
    for i,d in enumerate(products_data):
        if(products_data[i]['price_inr']=='' or products_data[i]['avg_rating']=='' or products_data[i]['num_ratings']==''):
            amb.append(products_data[i])
    for a in amb:
        products_data.remove(a)
    price_all = np.array([float(d['price_inr'].strip().replace(',','').replace('₹','')) for d in products_data])
    avg_rating_all = np.array([float(d['avg_rating'].strip()) for d in products_data])
    num_ratings_all = np.array([int(d['num_ratings'].strip().replace(',','')) for d in products_data])
    med_price = np.median(price_all)
    max_price = np.max(price_all)
    max_avgr = np.max(avg_rating_all)
    max_numr = np.max(num_ratings_all)

    
    for item_list in products_data:
        price_inr = float(item_list['price_inr'].strip().replace(',',''))
        avg_rating = float(item_list['avg_rating'].strip().replace(',',''))
        num_ratings = int(item_list['num_ratings'].strip().replace(',',''))
        if(final_pass==False and np.abs(price_inr - med_price) >= med_price/2):
            score = -5.0
        else:
            # |score| < 1+1+1=3
            score = (price_inr/max_price)*wt_price + (avg_rating/max_avgr)*wt_avgr + (num_ratings/max_numr)*wt_numr
        item_list['score'] = score
    
    products_data_sorted = sorted(products_data, key=itemgetter('score'), reverse=True)
    for item_list in products_data_sorted:
        item_list['score'] = np.around(item_list['score'], 2)
    
    return products_data_sorted[:items_to_take]