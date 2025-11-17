import pandas as pd
from pathlib import Path
import glob

RAW = Path("data/raw")
OUT = Path("data/processed")

def clean_file(path):
    df = pd.read_csv(path)

    # FIX COLUMN NAMES FROM:
    # Date,_Close_,High,Low,Open,Volume
    df = df.rename(columns={
        "_Close_": "Close",
        "Date": "Date",
        "High": "High",
        "Low": "Low",
        "Open": "Open",
        "Volume": "Volume"
    })

    # Convert numeric columns
    numeric_cols = ["Close", "High", "Low", "Open", "Volume"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Add ticker
    df["Ticker"] = Path(path).stem

    return df

def main():
    frames = []
    for file in RAW.glob("*.csv"):
        print(f"Cleaning: {file}")
        cleaned = clean_file(file)
        frames.append(cleaned)

    final = pd.concat(frames, ignore_index=True)
    final.to_csv(OUT / "all_cleaned.csv", index=False)
    print("Saved: data/processed/all_cleaned.csv")

if __name__ == "__main__":
    main()
