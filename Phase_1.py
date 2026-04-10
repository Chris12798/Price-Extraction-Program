import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/danganronpa-volume-1_889/index.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

#print("product_page = " + url)

Book_url = (url)
#print(Book_url)

Product_page = soup.find(id="content_inner")
#print(Product_page)

Product_info = (soup.find(class_="table table-striped")).get_text()
#print(Product_info)

Product_code = (Product_page.find(class_="table table-striped")).find("td").get_text()
#print("universal_product_code = " + Product_code)

UPC = (Product_code)
#print(UPC)

Title = Product_page.find(class_="col-sm-6 product_main").find("h1").get_text()
#print("book_title = " + Book_title)
Book_title = (Title)
#print(Book_title)

price_with_tax = (Product_page.find(class_="table table-striped")).find_all("td")[2].get_text()
#print("price_including_tax = " + Price_including_tax)
Price_including_tax = (price_with_tax)
#print(Price_including_tax)

price_no_tax = (Product_page.find(class_="table table-striped")).find_all("td")[3].get_text()
#print("price_excluding_tax = " + Price_excluding_tax)
Price_excluding_tax = (price_no_tax)
#print(Price_excluding_tax)

Quantity = (Product_page.find(class_="table table-striped")).find_all("td")[5].get_text()
#print("quantity_available = " + Quantity_available)
Quantity_available = (Quantity)
#print(Quantity_available)

Desc = Product_page.find(id="product_description").find_next_sibling("p").get_text()
#print("product_description = " + Product_description)
Product_description = (Desc)
#print(Product_description)

Book_category = soup.find("ul", class_="breadcrumb").find_all("li")
#print("Book_category[2].get_text(strip=True))
Category = (Book_category[2].get_text(strip=True))
#print(Category)

Rating = Product_page.find("p", class_="star-rating")["class"][1]
#print("review_rating = " + Rating + " stars")
Review_rating = (Rating + " stars")
#print(Review_rating)

Image = Product_page.find(class_="item active").find("img")["src"]
#print("image_url = " + "https://books.toscrape.com/" + Image)
Image_url = ("https://books.toscrape.com/" + Image)
#print(Image_url)

book_data = pd.DataFrame(
    {
        "product_page_url": [Book_url],
        "universal_product_code (upc)": [UPC],
        "book_title": [Book_title],
        "price_including_tax": [Price_including_tax],
        "price_excluding_tax": [Price_excluding_tax],
        "quantity_available": [Quantity_available],
        "product_description": [Product_description],
        "category": [Category],
        "review_rating": [Review_rating],
        "image_url": [Image_url]
    })

print(book_data)

book_data.to_csv("Danganronpa_Volume_1.csv")