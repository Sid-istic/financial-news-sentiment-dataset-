import requests
from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf
from datetime import datetime
import time
import random
import csv



# Top 100 Indian stocks (Nifty 50 + Next 50)
nifty_100 = [
    'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'HINDUNILVR.NS',
    'ICICIBANK.NS', 'KOTAKBANK.NS', 'BHARTIARTL.NS', 'LT.NS', 'ITC.NS',
    'SBIN.NS', 'BAJFINANCE.NS', 'HCLTECH.NS', 'ASIANPAINT.NS', 'MARUTI.NS',
    'TITAN.NS', 'SUNPHARMA.NS', 'AXISBANK.NS', 'M&M.NS', 'ULTRACEMCO.NS',
    'WIPRO.NS', 'NESTLEIND.NS', 'POWERGRID.NS', 'NTPC.NS', 'TECHM.NS',
    'ADANIPORTS.NS', 'JSWSTEEL.NS', 'BAJAJFINSV.NS', 'GRASIM.NS', 'TATASTEEL.NS',
    'ONGC.NS', 'DIVISLAB.NS', 'COALINDIA.NS', 'IOC.NS', 'SHREECEM.NS',
    'HDFCLIFE.NS', 'UPL.NS', 'BPCL.NS', 'INDUSINDBK.NS', 'DRREDDY.NS',
    'CIPLA.NS', 'EICHERMOT.NS', 'HEROMOTOCO.NS', 'BRITANNIA.NS', 'GAIL.NS',
    'BAJAJ-AUTO.NS', 'TATAMOTORS.NS', 'HINDALCO.NS', 'VEDL.NS', 'PFC.NS',
    # Next 50
    'DABUR.NS', 'HAVELLS.NS', 'AMBUJACEM.NS', 'PIDILITIND.NS', 'BERGEPAINT.NS',
    'GODREJCP.NS', 'AUROPHARMA.NS', 'ZYDUSLIFE.NS', 'BOSCHLTD.NS', 'ASHOKLEY.NS',
    'BANDHANBNK.NS', 'BHARATFORG.NS', 'BIOCON.NS', 'CHOLAFIN.NS', 'COLPAL.NS',
    'CONCOR.NS', 'DLF.NS', 'GODREJPROP.NS', 'HINDPETRO.NS', 'ICICIPRULI.NS',
    'IGL.NS', 'INDUSTOWER.NS', 'JINDALSTEL.NS', 'LUPIN.NS', 'UNITDSPR.BO',
    'MRF.NS', 'OFSS.NS', 'PETRONET.NS', 'PIIND.NS', 'SAIL.NS', 'SRF.NS',
    'SIEMENS.NS', 'TORNTPHARM.NS', 'TORNTPOWER.NS', 'TVSMOTOR.NS', 'UBL.NS',
    'MOTHERSON.NS', 'ACC.NS', 'ADANIENSOL.NS', 'APOLLOHOSP.NS', 'APOLLOTYRE.NS',
    'BATAINDIA.NS', 'BPCL.NS', 'COFORGE.NS', 'ESCORTS.NS', 'EXIDEIND.NS',
    'GLENMARK.NS', 'IPCALAB.NS', 'LICHSGFIN.NS', 'MANAPPURAM.NS', 'MARICO.NS'
]



USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
]




def fetch_headlines(tickers):
    url = "https://news.google.com/rss/search?q="
    headlines = {}
    for ticker in tickers:
        try:
            headers = {
                'User-Agent': random.choice(USER_AGENTS)
            }
            ticker = ticker.replace('.NS', '').replace('.BO','') # Clean ticker symbol
            print(f"Fetching headlines for {ticker}...")
            response = requests.get(url+ticker+"+financial&hl=en-IN&gl=IN&ceid=IN:en",headers=headers)
            soup = BeautifulSoup(response.content, 'xml')
            titles = [title.text for title in soup.find_all('title')]
            Dates = [pubDate.text for pubDate in soup.find_all('pubDate') ]
            pubDates = [datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d') for date in Dates] # converting date time to desired format which is YYYY-MM-DD
            info = list(zip(titles[2:], pubDates))
            headlines[ticker] = info  
            time.sleep(random.uniform(5, 10))  # Random delay to avoid rate limiting
        except Exception as e:
            print(f"Error fetching headlines for {ticker}: {e}")
            headlines[ticker] = []
    
    return headlines

def save_headlines_to_csv(headlines, filename):
    i = 0
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Ticker', 'Headline', 'Date'])
        for ticker, articles in headlines.items():
            for headline, date in articles:
                writer.writerow([ticker, headline, date])
                i += 1
    print(f"Total articles saved: {i}")

def main():
    headlines = fetch_headlines(nifty_100)
    save_headlines_to_csv(headlines, 'D:/Stock Movement/data/raw_data/nifty_100_headlines.csv')
    print(f"Headlines saved to CSV {len(headlines)} tickers processed.")


if __name__ == "__main__":
    main()
    print("All tasks completed successfully.")

