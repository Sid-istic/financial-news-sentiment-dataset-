
# 📈 Indian Financial News Sentiment Dataset (NSE/BSE)

This repo documents the full pipeline I built to create a high-quality, India-specific dataset that links **financial news headlines** with **stock price movement**.  
The dataset is designed to support **sentiment analysis**, **fine-tuning financial LLMs**, and **causality modeling**.

---

## 🧠 What This Project Does

- Scrapes financial news from Google News
- Collects historical stock prices (NSE/BSE) via `yfinance`
- Prepares a dataset linking headlines to 1D/3D/5D returns
- Applies sentiment scoring using a FinBERT-based transformer
- Allows manual correction and relabeling for fine-tuning
- Tracks outliers, mismatches, and enables exploratory data analysis

---

## 📁 File Structure

```bash
.
├── 01_scraping_raw_data.py
├── 02_dataset_preparation.py
├── 03_data_cleaning_sentiment_scoring.ipynb
├── 04_EDA.ipynb
└── data/
    ├── raw/             # Unprocessed scraped data
    ├── processed/       # Cleaned + structured data
    └── labeled/         # Final manually labeled dataset (973 rows)
