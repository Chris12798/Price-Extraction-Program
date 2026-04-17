![Static Badge](https://img.shields.io/badge/github-repo-blue)

# Price-Extraction-Program
Beta version of a price monitoring system for an online retailer. Containing four phases, this web scraper extracts book data from [BooksToScrape](https://books.toscrape.com/index.html) and stores it in a structured csv file while also downloading book cover images locally. Each phase of the program progresses from scraping a single book to scraping every book on the entire website. 

## 🧠 What This Program Does

1. Looks at [BooksToScrape](https://books.toscrape.com/index.html)
2. Collects book details such as:
  - Product page URL
  - Universal Product Code (UPC)
  - Title
  - Price w/ and w/out tax
  - Quantity
  - Category
  - Rating
  - Description
  - Image URL
3. Saves everything into a spreadsheet (CSV file)
4. Downloads book cover images

## 📓 Phases

There are four phases associated with this scraper that shows the evolution of the code. Each phase builds on top of each other to get the completed scraper, **"Phase_4.py"**

**Phase 1: Single Book**

Scrapes one book and saves it to a CSV.

**Phase 2: Category**

Scrapes all books from one category (Sequential Art).

**Phase 3: Full Website**

Scrapes all books across all categories.

**Phase 4: Images**

Scrapes all books across all categories then downloads every book image and stores them locally.

## ⚙️ Requirements
- Python
- pandas
- requests
- BeautifulSoup (bs4)

## ⚙️ Installation Guide

**1. Install Python**

👉 Download [Python](https://www.python.org/downloads/) here.

**2. Download the scraper on GitHub**
  - Click the green Code button → Download ZIP → Extract the contents from the folder

**3. Install each library**
  - Open Terminal / Command Prompt or code editor of your choosing

Use the package manager [pip](https://pip.pypa.io/en/stable/) to learn more and install pandas, requests, and BeautifulSoup.

👇 Here is how to install each library:
```bash
pip install pandas
```
```bash
pip install requests
```
```bash
pip install BeautifulSoup
```

**4. Run the Program**

You can run the scraper for each phase by using this command:

```bash
python Phase_1.py
```

To check the other phases replace Phase_1.py with any of the other phases included in the zip folder.

> [!NOTE]
**Phase_4.py** is the completed code for the scraper and should be used to get all the data, csv excel file, and cover image for every book. 

**5. Output**

After running **Phase_4.py**, the program will:

1. Start scraping book data from the website
2. Download book images into a folder called "book_images"
3. Create a csv file called "all_books_data.csv"

👇 Here's an example of what the output for one book should look like for the first few columns:

```bash
book_title                product_page_url           universal_product_code     price_including_tax
It's Only the Himalayas   https://books.toscra...    a22124811bfa8350           Â£45.17
```

**Congratulations! You have successfully ran the program!** 😄

## 🗒️ Notes

> [!IMPORTANT]
The command below creates a delay when scraping the contents so it doesn’t overload the website. It's important to always have this so your IP doesn't get blocked for sending too many requests to the site too quickly. 

```bash
time.sleep(1)
```

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)
