import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_data():
    # Setup Chrome options (Headless mode for background processing)
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        print("Loading IMDb Top 250...")
        driver.get("https://www.imdb.com/chart/top/")
        time.sleep(5)  # Wait for dynamic content
        
        movies = []
        # Locate movie items
        items = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
        
        print(f"Found {len(items)} movies. Starting extraction...")
        
        for index, item in enumerate(items[:250]):
            try:
                # Extract Title
                title_el = item.find_element(By.CSS_SELECTOR, "h3.ipc-title__text")
                title = title_el.text.split(". ", 1)[-1] # Remove ranking number
                
                # Extract Metadata (Year is usually the first item)
                metadata = item.find_elements(By.CSS_SELECTOR, "span.cli-title-metadata-item")
                year = metadata[0].text if metadata else "N/A"
                
                # Extract Rating
                rating_el = item.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating")
                rating = float(rating_el.text)
                
                movies.append({"Rank": index + 1, "Title": title, "Year": year, "Rating": rating})
            except Exception as e:
                continue

        # Save to CSV
        df = pd.DataFrame(movies)
        df.to_csv("imdb_top_250.csv", index=False)
        print("Data saved to 'imdb_top_250.csv'")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_data()