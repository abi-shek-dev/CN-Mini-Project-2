import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="IMDb Top 250 Dashboard", layout="wide")

# 2. Load Data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("imdb_top_250.csv")
        # Ensure 'Year' is treated as numeric (clean up any non-numeric chars if needed)
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        return df
    except FileNotFoundError:
        return pd.DataFrame()

df = load_data()

# 3. Dashboard Layout
st.title("🎬 IMDb Top 250 Movies Analysis")
st.markdown("This dashboard visualizes data scraped from the IMDb Top 250 list.")

if df.empty:
    st.error("No data found! Please run 'scraper.py' first to generate the CSV file.")
else:
    # --- Top KPIs ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Movies Scraped", len(df))
    col2.metric("Average Rating", round(df['Rating'].mean(), 2))
    col3.metric("Oldest Movie Year", int(df['Year'].min()))

    st.divider()

    # --- Visualization 1: Rating Distribution ---
    st.subheader("📊 Distribution of IMDb Ratings")
    fig_hist = px.histogram(df, x="Rating", nbins=20, title="How are movies rated?", color_discrete_sequence=['#E50914'])
    st.plotly_chart(fig_hist, use_container_width=True)

    # --- Visualization 2: Movies per Decade ---
    st.subheader("📅 Movies by Release Year")
    # Bin years into decades for cleaner viewing
    df['Decade'] = (df['Year'] // 10) * 10
    decade_counts = df['Decade'].value_counts().reset_index()
    decade_counts.columns = ['Decade', 'Count']
    decade_counts = decade_counts.sort_values('Decade')
    
    fig_bar = px.bar(decade_counts, x='Decade', y='Count', title="Which decades produced the most Top 250 movies?")
    st.plotly_chart(fig_bar, use_container_width=True)

    # --- Visualization 3: Top 10 Table ---
    st.subheader("🏆 Top 10 Highest Rated Movies")
    st.dataframe(df.nsmallest(10, 'Rank')[['Rank', 'Title', 'Year', 'Rating']], hide_index=True)

    # --- Raw Data ---
    with st.expander("View Full Raw Data"):
        st.dataframe(df)