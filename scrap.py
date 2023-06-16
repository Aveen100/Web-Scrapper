# import requests
# from bs4 import BeautifulSoup


# def get_product_info(url):
#     # Send a request to the URL and get the HTML content
#     response = requests.get(url)
#     content = response.content

#     # Parse the HTML content using Beautiful Soup
#     soup = BeautifulSoup(content, 'html.parser')

#     # Extract the product information
#     product_name = soup.find('span', {'id': 'productTitle'}).text.strip()
#     product_price = soup.find('span', {'class': 'a-price-whole'}).text.strip()
#     product_image = soup.find('img', {'id': 'landingImage'})['data-old-hires']

#     # Return the product information as a dictionary
#     return {
#         'name': product_name,
#         'price': product_price,
#         'image': product_image
#     }


# ****************** NEw ********************** *

# from flask import Flask, request
# from bs4 import BeautifulSoup
# import requests

# app = Flask(__name__)

# @app.route('/scrape')
# def scrape():
#     product_link = request.args.get('link')
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
#     }
#     response = requests.get(product_link, headers=headers)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     title = soup.find('span', {'id': 'productTitle'}).text.strip()
#     price = soup.find('span', {'class': 'a-price-whole'}).text.strip()
#     image = soup.find('img', {'alt': title})['src']
#     return {'title': title, 'price': price, 'image': image}

# if __name__ == '__main__':
#     app.run()




# ************************ NEw 2 ****************** *
import requests
from bs4 import BeautifulSoup

def scrape_amazon_page(url):
    # Make a GET request to the Amazon page
    response = requests.get(url)
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the product title and price from the page
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()
    
    return {'title': title, 'price': price}
