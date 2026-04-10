import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://books.toscrape.com/"

def scrape_one_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    Product_page = soup.find(id="content_inner")
    
    # Book URL
    Book_url = (url)

    # UPC
    Product_code = (Product_page.find(class_="table table-striped")).find("td").get_text()
    UPC = (Product_code)
        
    # Title
    Title = Product_page.find(class_="col-sm-6 product_main").find("h1").get_text()
    Book_title = (Title)

    # Price including tax
    price_with_tax = (Product_page.find(class_="table table-striped")).find_all("td")[2].get_text()
    Price_including_tax = (price_with_tax)

    # Price excluding tax
    price_no_tax = (Product_page.find(class_="table table-striped")).find_all("td")[3].get_text()
    Price_excluding_tax = (price_no_tax)
        
    # Description
    Desc = Product_page.find(id="product_description").find_next_sibling("p").get_text()
    Product_description = (Desc)

    # Quantity available
    Quantity = (Product_page.find(class_="table table-striped")).find_all("td")[5].get_text()
    Quantity_available = (Quantity)

    # Category
    Book_category = soup.find("ul", class_="breadcrumb").find_all("li")
    Category = (Book_category[2].get_text(strip=True))

    # Rating
    Rating = Product_page.find("p", class_="star-rating")["class"][1]
    Review_rating = (Rating + " stars")
        
    # Image
    Image = Product_page.find(class_="item active").find("img")["src"]
    Image_url = BASE_URL + Image.replace("../", "")
    
    return {
    "book_title": Book_title,
    "product_page_url": Book_url,
    "universal_product_code (upc)": UPC,
    "price_including_tax": Price_including_tax,
    "price_excluding_tax": Price_excluding_tax,
    "quantity_available": Quantity_available,
    "product_description": Product_description,
    "category": Category,
    "review_rating": Review_rating,
    "image_url": Image_url
}

# data = scrape_one_page(url)
# print(data)

def scrape_sequential_arts_data():
    sequential_arts_books = []

    for page_num in range(1,6):
        url = f"{BASE_URL}catalogue/category/books/sequential-art_5/page-{page_num}.html"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        books = soup.find_all('article', class_='product_pod')
    
        for book in books:
            a_link = book.find("a")["href"]
            book_url = BASE_URL + "catalogue/" + a_link.replace("../../../", "")
            
            try:
                data = scrape_one_page(book_url)
                sequential_arts_books.append(data)

                print(f"Scraped: {data['book_title']}")
                time.sleep(1)
            
            except Exception as e:
                print(f"Error scraping {book_url}: {e}")

    return sequential_arts_books

data = scrape_sequential_arts_data()
df = pd.DataFrame(data)
# print(df.head())

df.to_csv("sequential_arts_books.csv", index=False)



