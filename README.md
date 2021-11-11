# Book price comparison

tech: BeautifulSoup, requests, icecream<br>
version: 1.1.1

## Overview

Book price comparison via multiple online bookshops for Amazxn alternatives returning best price for each stores. 

Current list of stores (to be completed):
+ AbeBooks
+ Amazxn
+ Barnes & Noble
+ Biblio

## Dependencies

1. Create a virtual environment :

        python3 -m venv virtual
        
2. Activate the virtual environment :

    on Linux / Mac OS:

        source virtual/Scripts/activate
        
    on Windows:
        
        .\virtual\Scripts\activate
        
3. Install the necessary librairies :

        pip install beautifulsoup4 requests icecream

## Improvements

Following improvements are planned in the future :

v1.2:
+ take into account the delivery fee
+ add other bookstores
+ option for displaying prices in different currencies

v2.1:
+ return distance of delivery according to user's location and calculate carbon footprint
+ flag non-respectful companies
