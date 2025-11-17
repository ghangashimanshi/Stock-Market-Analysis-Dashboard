import pandas as pd
from pathlib import Path

INPUT = "data/processed/all_cleaned.csv"
OUTPUT = "data/processed/all_features.csv"

def add_features(df):

    # Ensure numeric
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df["Open"] = pd.to_numeric(df["Open"], errors="coerce")
    df["High"] = pd.to_numeric(df["High"], errors="coerce")
    df["Low"] = pd.to_numeric(df["Low"], errors="coerce")

    # 1. Daily Return (SAFE)
    df["Return"] = df.groupby("Ticker")["Close"].pct_change()

    # 2. Cumulative Return (SAFE)
    df["Cumulative_Return"] = (
        df.groupby("Ticker")["Return"]
        .transform(lambda x: (1 + x.fillna(0)).cumprod() - 1)
    )

    # 3. Peak (highest cumulative return so far)
    df["Peak"] = (
        df.groupby("Ticker")["Cumulative_Return"]
        .transform(lambda x: x.cummax())
    )

    # 4. Drawdown (SAFE)
    df["Drawdown"] = (df["Cumulative_Return"] - df["Peak"]) / df["Peak"]

    # 5. Volatility (30-day rolling std)
    df["Volatility"] = (
        df.groupby("Ticker")["Return"]
        .rolling(window=30)
        .std()
        .reset_index(level=0, drop=True)
        * (252 ** 0.5)
    )
    return df


def main():
    print("Loading cleaned dataset...")
    df = pd.read_csv(INPUT, parse_dates=["Date"])

    print("Adding features...")
    final_df = add_features(df)

    print("Saving processed dataset...")
    final_df.to_csv(OUTPUT, index=False)
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    main()
