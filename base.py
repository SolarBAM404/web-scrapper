# Imports
import requests
from bs4 import BeautifulSoup
import csv

testDataUrl = "https://www.claires.com/search/?q=Squishmallows"

def __main__():
    request = requests.get(testDataUrl)
    
    soup = BeautifulSoup(request.content, 'html.parser')
    
    results = soup.find_all("div", class_="product-tile")
    
    with open('products.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', 
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Product Name", "Price"])
        for result in results:
            product_name = result.find("div", class_="product-name")
            product_price = result.find("div", class_="product-pricing")
            writer.writerow([product_name.text.strip(), product_price.text.strip()])
        
if __name__ == "__main__":
    __main__()
