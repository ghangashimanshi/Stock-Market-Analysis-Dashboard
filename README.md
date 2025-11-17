# Stock Market Analysis Dashboard

A Python + Power BI project that downloads historical stock data, engineers trading features,  
and visualizes them in an interactive dashboard for quick performance, risk, and trend analysis.

---

### 🚀 Key Features

✔️ Automatically downloads historical stock data (AAPL, AMZN, GOOGL, META, MSFT, NVDA)  
✔️ Cleans, preprocesses, and merges raw datasets  
✔️ Generates trading indicators (Returns, Drawdown, Moving Averages, Volatility)  
✔️ Creates a master `all_features.csv` dataset for analysis  
✔️ Interactive Power BI dashboard with:
   - Performance KPIs (Cumulative Return, Max Drawdown, Latest Price)
   - Risk vs Return Bubble Chart
   - Monthly Returns Heatmap
   - Moving Average Trend Charts (MA30, MA7, MA90)
   - Volatility Tracking
   - Ticker Summary Table
✔️ Fully reproducible using Python scripts


---

#### 📁 Project Structure

Stock Market Analysis Dashboard/
│
├── data/
│ ├── raw/ # Original downloaded stock CSVs
│ ├── processed/ # Cleaned & engineered datasets
│
├── scripts/
│ ├── fetch_data.py # Downloads stock price data
│ ├── clean_data.py # Cleans & merges raw CSVs
│ ├── features.py # Generates indicators (MA, Returns, Volatility, etc.)
│
├── notebooks/ # Jupyter notebooks (optional)
│
├── power_bi/ # Power BI report files (.pbix, screenshots)
│
├── requirements.txt # Python dependencies
├── README.md
└── .gitignore

---

##### ⚙️ Installation & Setup

###### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ghangashimanshi/Stock-Market-Analysis-Dashboard.git
cd Stock-Market-Analysis-Dashboard

Create Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows

Install Dependencies

pip install -r requirements.txt

Run Python Scripts (If you want to regenerate data)

➤ Download Raw Stock Data
python scripts/fetch_data.py

➤ Clean & Merge Data
python scripts/clean_data.py

➤ Generate Indicators (Returns, MA, Drawdown, Volatility)
python scripts/features.py

🟦 4️⃣ Power BI Dashboard

Once data is processed, open the dashboard:

📁 power_bi/Stock_Market_Dashboard.pbix

This dashboard includes:

| Visualization                    | Purpose                                       |
| -------------------------------- | --------------------------------------------- |
| Performance KPIs                 | Latest Close, Cumulative Return, Max Drawdown |
| Risk-Return Scatter Plot         | Compare asset risk vs expected returns        |
| Monthly Volume & Returns         | Seasonal trends in price movement             |
| Volatility Chart                 | Track price volatility over time              |
| MA30 / MA7 / MA90 Price Trends   | Identify crossover trading signals            |
| Monthly Returns Heatmap          | Detect strong & weak months                   |
| Ticker Summary Table             | Side-by-side stats for all stocks             |

➡ You can update visuals anytime without changing Python scripts.

🟩 5️⃣ Technologies Used

| Category          | Tools                               |
| ----------------- | ----------------------------------- |
| Language          | Python                              |
| Data Source       | Yahoo Finance                       |
| Libraries         | pandas, numpy, yfinance, matplotlib |
| BI Tool           | Microsoft Power BI                  |
| Version Control   | Git & GitHub                        |

🟪 6️⃣ License

📜 This project is open-source.
Feel free to use, modify, and share.
