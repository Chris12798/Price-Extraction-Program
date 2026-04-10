import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import os
import re
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
# Directory to save images
SAVE_DIR = "book_images"

# Create directory to store images if it doesn't exist
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def sanitize_filename(name, max_length=200): # Function to sanitize filenames for Windows

    # 1. Remove characters that are NOT allowed in Windows filenames
    name = re.sub(r'[\\/*?:"<>|]', "", name)

    name = name.strip()

    name = name.rstrip(".")

    name = name.replace(" ", "_")

    # 5. Windows reserved filenames (cannot be used as file names)
    reserved_names = [
        "CON", "PRN", "AUX", "NUL",
        "COM1", "COM2", "COM3", "COM4", "COM5",
        "COM6", "COM7", "COM8", "COM9",
        "LPT1", "LPT2", "LPT3", "LPT4", "LPT5",
        "LPT6", "LPT7", "LPT8", "LPT9"
    ]

    if name.upper() in reserved_names:
        name = "_" + name

    # 6. Limit filename length to prevent issues with very long names
    name = name[:max_length]

    return name

# Function to download the image and save it
def download_image(image_url, image_name):
    try:
        response = requests.get(image_url)
        response.raise_for_status() # Check if the request was successful

        file_path = os.path.join(SAVE_DIR, image_name) 

        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"Downloaded: {image_name}")

    except requests.exceptions.RequestException as e:
        print(f"Download error: {e}")

# Function to scrape one book's data
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
    desc_tag = Product_page.find(id="product_description")

    if desc_tag:
        Product_description = desc_tag.find_next_sibling("p").get_text()
    else:
        Product_description = ""

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
    Image_src = Product_page.find(class_="item active").find("img")["src"]
    Image_url = urljoin(BASE_URL, Image_src)

    # Sanitize the filename for the image
    Image_name = sanitize_filename(f"{Book_title}") + ".jpg"

    print("IMAGE URL:", Image_url)

    # Download image
    download_image(Image_url, Image_name)

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

#def main(): # Removed main function to test single book scraping
    print("Testing single book...")

    test_url = "https://books.toscrape.com/catalogue/sharp-objects_997/index.html"

    data = scrape_one_page(test_url)

    print(data)

#if __name__ == "__main__":
    main()

# Function to scrape books from sequential art category
def scrape_sequential_arts_data():
    sequential_arts_books = []

    for page_num in range(1, 6):
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

# Function to get all categories
def get_all_categories():
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    category_section = soup.find("ul", class_="nav nav-list").find("ul")
    categories = category_section.find_all("a")

    category_links = []
    
    for cat in categories:
        name = cat.get_text(strip=True)
        href = cat["href"]
        full_url = BASE_URL + href
        
        category_links.append({
            "name": name,
            "url": full_url
        })
    
    return category_links

# Function to scrape a specific category
def scrape_category(category):
    books_data = []
    page_num = 1

    while True:
        
        if page_num == 1:
            url = category["url"]
        else:
            url = category["url"].replace("index.html", f"page-{page_num}.html")
        
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        books = soup.find_all('article', class_='product_pod')

        if not books:
            break

        for book in books:
            a_link = book.find("a")["href"]
            book_url = BASE_URL + "catalogue/" + a_link.replace("../../../", "")

            try:
                data = scrape_one_page(book_url)
                books_data.append(data)
                print(f"{category['name']} - {data['book_title']}")
                time.sleep(1)

            except Exception as e:
                print(f"Error scraping {book_url}: {e}")

        page_num += 1

    return books_data

# Function to scrape all books from all categories
def scrape_all_books():
    all_books = []
    categories = get_all_categories()
    
    for category in categories:
        category_data = scrape_category(category)
        all_books.extend(category_data)
    
    return all_books

# Main function to execute the scraping process and save data to CSV
def main():
    print("Starting to scrape all books...")

    all_books_data = scrape_all_books()

    print("Finished scraping all books. Saving data to CSV...")

    df = pd.DataFrame(all_books_data)
    df.to_csv("all_books_data.csv", index=False)
    print(df.head())

    print("Scraping completed. Data saved to all_books_data.csv")

if __name__ == "__main__":
    main()
