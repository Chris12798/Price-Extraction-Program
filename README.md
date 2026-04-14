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

## ⚙️ Installation Guide

**1. Install Python**

👉 Download [Python](https://www.python.org/downloads/) here.

**2. Download the project**

## ⚙️ Requirements
- Python
- pandas
- requests
- BeautifulSoup (bs4)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to learn more and install pandas, requests, and BeautifulSoup.

Here is how to install each library:
```bash
pip install pandas
```
```bash
pip install requests
```
```bash
pip install BeautifulSoup
```

## 📓 Phases
**Phase 1: Single Book**

Scrapes one book and saves it to a CSV.

**Phase 2: Category**

Scrapes all books from one category (Sequential Art).

**Phase 3: Full Website**

Scrapes all books across all categories.

**Phase 4: Images**

Downloads book images and stores them locally.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)
