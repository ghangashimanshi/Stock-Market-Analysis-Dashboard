import argparse
import yfinance as yf
from pathlib import Path
import pandas as pd

def fetch(tickers, start, end, out_dir="data/raw"):
    # Ensure output directory exists
    Path(out_dir).mkdir(parents=True, exist_ok=True)

    for ticker in tickers:
        print(f"Downloading data for: {ticker}")
        data = yf.download(ticker, start=start, end=end, progress=False)

        if data.empty:
            print(f"⚠️ Warning: No data returned for {ticker}")
            continue

        # Reset index to turn Date into a column
        data.reset_index(inplace=True)

        # Save to CSV
        filepath = Path(out_dir) / f"{ticker}.csv"
        data.to_csv(filepath, index=False)
        print(f"Saved: {filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--tickers", nargs="+", required=True, help="List of stock tickers")
    parser.add_argument("--start", default="1989-01-01", help="Start date")
    parser.add_argument("--end", default="2023-12-31", help="End date")

    args = parser.parse_args()

    fetch(args.tickers, args.start, args.end)
