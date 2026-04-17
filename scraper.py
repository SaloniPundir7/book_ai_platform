
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import timedelta
import time

# Django setup
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from books.models import Book
from selenium.webdriver.chrome.service import Service


def scrape_books():
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    
    driver.get("https://books.toscrape.com/")

    time.sleep(3)

    books = driver.find_elements(By.CLASS_NAME, "product_pod")

    for book in books[:10]:  # scrape first 10 books
        title = book.find_element(By.TAG_NAME, "h3") \
            .find_element(By.TAG_NAME, "a") \
            .get_attribute("title")
        price = book.find_element(By.CLASS_NAME, "price_color").text
        
        try:
           rating_class = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
           rating = rating_class.split()[-1]  # gives One, Two, Three...
        except:
            rating = "0"

        Book.objects.create(
            title=title,
            author="Unknown",
            description=f"Price: {price}",
            rating=0,
            url="https://books.toscrape.com/"
        )

    driver.quit()
    print("Scraping Done!")


if __name__ == "__main__":
    scrape_books()