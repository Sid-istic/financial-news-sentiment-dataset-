# financial-news-sentiment-dataset
# 📊 Indian Financial News Sentiment & Stock Movement Dataset

A high-quality, manually-labeled dataset that links **Indian financial news headlines** to **stock price movements** — designed for **NLP + Time Series** tasks like:

- Financial sentiment analysis  
- Stock movement correlation  
- Causality modeling (Granger, transfer entropy)  
- Fine-tuning transformer models on Indian financial tone  

---

## 🧠 What’s Inside?

| Column         | Description |
|----------------|-------------|
| `Ticker`       | NSE-listed stock symbol |
| `Headline`     | Financial news headline from Google News |
| `Date`         | Date of the headline |
| `Close`        | Closing price of the stock on that date (from yfinance) |
| `1d_return`    | % return after 1 trading day |
| `3d_return`    | % return after 3 trading days |
| `5d_return`    | % return after 5 trading days |
| `sentiment`    | Sentiment label (`positive`, `neutral`, `negative`) |
| `source_score` | Model-predicted confidence score (FinancialBERT) |
| `max_abs_return` | Maximum absolute return across 1D, 3D, and 5D |


---

## ✅ Key Features

- 🇮🇳 **Indian Market Focus** — Most financial sentiment datasets are US/EU-centric. This one is built for **NSE/BSE stocks**.
- 🗞️ **6,000+ headlines** from **Google News**
- 📈 Linked to years of **daily stock price history** via yFinance
- 🧠 Includes **manual sentiment labels** for 1000+ headlines
- 🧪 Designed for **fine-tuning** transformer-based financial models (e.g. FinBERT, DeBERTa)
- ⚡ Includes `max_abs_return` to identify high-signal market reactions

---

## 🔍 Data Collection & Processing

- **News Source**: Scraped via Google News with company + financial keywords
- **Stock Prices**: Fetched using [`yfinance`](https://pypi.org/project/yfinance/)
- **Return Calculation**: Standard % change for 1D, 3D, and 5D horizons
- **Sentiment Labels**:
  - Initially predicted using `ahmedrachid/FinancialBERT-Sentiment-Analysis`
  - 1000+ headlines manually reviewed and corrected for quality
- **Outliers & Edge Cases**: Rows where sentiment ≠ price movement are included for research

---

## 💼 Use Cases

- Train domain-specific sentiment models for India
- Build RAG pipelines for stock analytics
- Analyze whether sentiment causes price movements (Granger, VAR)
- Train LSTM or hybrid models for stock forecasting

---

## 📂 Example Row

```csv
Ticker,Headline,Date,Close,1d_return,3d_return,5d_return,sentiment,score,max_abs_return
INFY,Infosys reports 12% decline in profit amid global slowdown,2024-07-12,1425.30,-2.18,-1.75,-0.94,negative,0.984,2.18
```
## 📌 License

This dataset is released under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share, use, and build upon this dataset — even commercially — as long as you credit the original creator:

**Siddharth Pratap Singh**
