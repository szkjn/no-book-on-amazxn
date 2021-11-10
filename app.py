from bs4 import BeautifulSoup
import requests
from icecream import ic
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

ic.configureOutput(prefix=' Debug | ')

def leboncoin(keyword):
    
    keyword = keyword.replace(' ', '+')
    leboncoin=f'https://www.leboncoin.fr/recherche?text={keyword}'
    
    res = requests.get(leboncoin)
    
    print(leboncoin)
    
    print('Searching LeBonCoin ...')
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())
    
def amazon(keyword):

    keyword2 = keyword.replace(' ', '+').replace("'", '%27')
    amazon_search=f'https://www.amazon.fr/"{keyword2}"/s?k="{keyword2}"'
    
    res = requests.get(amazon_search, headers=headers)
    
    ic(amazon_search)
    print('\nSearching Amazon ...\n |')
    
    soup = BeautifulSoup(res.text,'html.parser')
    
    try:
        results = soup.select('.s-asin')
        ic(len(results))
        
        sponsored = soup.select('.s-label-popover-hover')
        prices = []
        links = []

        for result in results:
            
            # removing sponsored item
            if sponsored[0].text in result.text:
                results.remove(result)
                ic('filtering: sponsored link')
                continue
            
            # keeping only exact keyword matches
            title = result.select('.a-link-normal.a-text-normal')[0].text
            if keyword.lower() not in title.lower(): 
                results.remove(result)
                continue
            
            # removing item without prices
            try:
                price = result.select('.a-price-whole')[0].getText()
                prices.append(float(price.replace(',', '.'))) 
                        
            except:
                ic('filtering: item without price')
                results.remove(result)
                continue
            
            link = result.select('.a-link-normal.a-text-normal')[0]['href']
            link = 'https://amazon.fr' + link
            links.append(link)

        ic(prices)
        
        best_price = min(prices)
        best_price_link = links[prices.index(best_price)]
        
        print(f' |  > Best Price: € {best_price}\n |_ > Link: {best_price_link}')
    except:
        print(' |_  No item found.')
    
def ebay(keyword):
    
    keyword2 = keyword.replace(' ', '+')
    ebay_search=f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw="{keyword2}"&_sacat=0'
    
    ic()
    res = requests.get(ebay_search, headers=headers)
    
    ic(ebay_search)
    print('\nSearching Ebay ...\n|')
    
    soup = BeautifulSoup(res.text,'html.parser')
    results = soup.select('.srp-results')
    
    ic(len(results))
    
def abebooks(keyword):
    
    keyword2 = keyword.replace(' ', '+')
    abebooks_search=f'https://www.abebooks.fr/servlet/SearchResults?cm_sp=SearchF-_-TopNavISS-_-Results&ds=20&kn="{keyword2}"&searchprefs=on&sts=t'

    res = requests.get(abebooks_search, headers=headers)
    
    ic(abebooks_search)
    print('\nSearching AbeBooks ...\n |')
    
    soup = BeautifulSoup(res.text,'html.parser')
    
    try:
        results = soup.select('.result-item')
        
        ic(len(results))
        
        prices = []
        links = []
        
        for result in results:
            
            # keeping only exact keyword matches
            title = result.select('.title')[0].text
            if keyword.lower() not in title.lower(): 
                results.remove(result)
                continue
            
            # removing item without prices
            try:
                price = result.select('.item-price')[0].text
                prices.append(float(price.strip('EUR ').replace(',', '.')))
            except:
                ic('filtering: item without price')
                results.remove(result)
                continue
            
            link = result.select('a')[0]['href']
            link = 'https://abebooks.fr' + link
            links.append(link)
        
        ic(len(results))

        ic(prices)
        
        best_price = min(prices)
        best_price_link = links[prices.index(best_price)]
        
        print(f' |  > Best Price: € {best_price}\n |_ > Link: {best_price_link}')
    
    except:
        print(' |_  No item found.')
    
def barnesandnoble(keyword):
       
    keyword2 = keyword.replace(' ', '+')
    barnesandnoble_search=f'https://www.barnesandnoble.com/s/{keyword2}'

    res = requests.get(barnesandnoble_search, headers=headers)
    
    ic(barnesandnoble_search)
    print('\nSearching Barnes & Noble ...\n |')
    
    soup = BeautifulSoup(res.text,'html.parser')
    
    try:
        results = soup.select('.product-shelf-tile')
        
        ic(len(results))
        
        prices = []
        links = []
        
        for result in results:
            
            # keeping only exact keyword matches
            title = result.select('a')[0]['title']
            if keyword.lower() not in title.lower(): 
                results.remove(result)
                continue
            
            # removing item without prices
            try:
                price = result.select('.current')[0].text
                price = re.findall("\d+\.\d+", price)[0] # extracts float from string
                prices.append(float(price))
            except:
                ic('filtering: item without price')
                results.remove(result)
                continue
            
            link = result.select('a')[0]['href']
            link = 'https://www.barnesandnoble.com/' + link
            links.append(link)
        
        ic(len(results))

        ic(prices, links)
        
        best_price = min(prices)
        best_price_link = links[prices.index(best_price)]
        
        print(f' |  > Best Price: $ {best_price}\n |_ > Link: {best_price_link}')
    
    except:
        print(' |_  No item found.')
    
    
def biblio(keyword):
    
    keyword2 = keyword.replace(' ', '+')
    barnesandnoble_search=f'https://www.biblio.com/search.php?stage=1&result_type=works&keyisbn={keyword2}'

    res = requests.get(barnesandnoble_search, headers=headers)
    
    ic(barnesandnoble_search)
    print('\nSearching Biblio ...\n |')
    
    soup = BeautifulSoup(res.text,'html.parser')
    
    try:
        results = soup.select('.results')[0].select('.item')
        
        ic(len(results))
        
        prices = []
        links = []

        for result in results:
                
            # keeping only exact keyword matches
            title = result.select('.title')[0].text
            if keyword.lower() not in title.lower(): 
                results.remove(result)
                continue
            
            # removing item without prices
            try:
                price = result.select('.item-price')[0].text
                price = re.findall("\d+\.\d+", price)[0] # extracts float from string
                prices.append(float(price))
            except:
                ic('filtering: item without price')
                results.remove(result)
                continue
            
            link = result.select('.title')[0].select('a')[0]['href']
            links.append(link)
            
        ic(len(results))

        ic(prices, links)
        
        best_price = min(prices)
        best_price_link = links[prices.index(best_price)]
        
        print(f' |  > Best Price: $ {best_price}\n |_ > Link: {best_price_link}\n')
    
    except:
        print(' |_  No item found.')
    
# ---------------------------------------------------------------------------------------   
    
def compare():
    
    book = input("What book do you wanna search for ?\n > ")
    abebooks(book)
    amazon(book)
    barnesandnoble(book)
    biblio(book)

book = 'automate the boring stuff with python'    

ic.disable()
# compare()

compare()
