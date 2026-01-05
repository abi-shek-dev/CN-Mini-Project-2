# 🎬 IMDb Movie Rating Scraper & Dashboard

## 📌 Project Description

The **IMDb Movie Rating Scraper** is a Python-based automation tool that
dynamically scrapes movie data from the IMDb Top 250 Movies list. It
utilizes **Selenium** and **Chrome WebDriver** to handle dynamic content
loading and extracts key details for analysis.

This project also includes an interactive **Streamlit Dashboard** to
visualize trends, allowing users to analyze movie ratings, release
years, and rankings efficiently.

## 🚀 Features

-   **Dynamic Movie Scraping:** Uses Selenium to load the IMDb Top 250
    page and extract full content.
-   **Data Extraction:** Retrieves Movie Title, Release Year, IMDb
    Rating, and Ranking.
-   **Headless Mode:** Configurable to run in the background without
    opening a browser window.
-   **Structured Output:** Automatically saves extracted data to a CSV
    file (`imdb_top_250.csv`) for easy access.
-   **Interactive Dashboard:** Visualizes the data using Streamlit and
    Plotly (Rating distribution, Movies per decade, Top 10 lists).

## 🛠️ Technologies Used

-   **Language:** Python
-   **Browser Automation:** Selenium, Chrome WebDriver
-   **Data Manipulation:** Pandas
-   **Visualization:** Streamlit, Plotly
-   **Utility:** WebDriver Manager, Time

## 📂 Project Structure

``` text
├── scraper.py
├── dashboard.py
├── requirements.txt
├── imdb_top_250.csv
└── README.md
```

## ⚙️ Installation

``` bash
git clone https://github.com/yourusername/imdb-scraper.git
cd imdb-scraper
```

### Virtual Environment

``` bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### Install Dependencies

``` bash
pip install -r requirements.txt
```

## 🖥️ Usage

### Run Scraper

``` bash
python scraper.py
```

### Run Dashboard

``` bash
streamlit run dashboard.py
```

## 🔮 Future Improvements

-   Scrape individual movie pages for cast & genre
-   Track rating changes over time
-   Add recommendation engine

## 📄 License

Open-source for educational purposes.
