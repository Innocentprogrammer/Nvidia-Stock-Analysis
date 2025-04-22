# 📈 NVIDIA Stock Trend Analysis

This project analyzes historical NVIDIA stock data to uncover trends, patterns, and key insights using Python and data visualization libraries.

---

## 📁 Folder Structure

```
Nvidia_Stock_Analysis/
│
├── nvidia_stock.csv              # Raw NVIDIA stock data
├── nvidia_stock_cleaned.csv      # Cleaned stock data
├── nvidia_analysis.py            # Python file with full analysis
├── README.md                     # Project overview and documentation
└── plots/                        # Saved visualizations
    ├── closing_price.png         # Line chart of closing prices
    ├── moving_avg.png            # 30-day simple moving average
    ├── daily_returns.png         # Daily return trend
    └── Correlation_Heatmap.png   # Correlation Heatmap
```

---

## 🧠 Objective

Analyze NVIDIA stock data to:

- Visualize historical trends
- Calculate daily returns and volatility
- Identify correlations
- Explore price movements and investor behavior

---

## 📊 Dataset Description

The dataset (`nvidia_stock.csv`) contains:

- `Date`: Date of the stock entry
- `Open`, `High`, `Low`, `Close`: Daily prices
- `Adj Close`: Adjusted closing price
- `Volume`: Number of shares traded

---

## 🔧 Tools & Libraries Used

- Python 🐍
- Pandas
- Matplotlib
- Seaborn
- Plotly (for interactive charts)

---

## 📈 Analysis Performed

1. **Data Cleaning**:

   - Handled missing values
   - Converted `Date` column to datetime
   - Set `Date` as index for time-series analysis

2. **Visualizations**:

   - **Closing Price Trend**: Line chart of stock closing prices
   - **30-Day SMA**: Rolling average to smooth short-term volatility
   - **Daily Returns**: Calculated & visualized price change percentage
   - **Correlation Heatmap**: Relationship between stock metrics
   - **Interactive Plot**: Created with Plotly for exploration

3. **Saved Plots**: Output graphs saved to `plots/` folder

---

## 📌 Key Insights

- Identified upward/downward trends in stock performance
- Evaluated short-term vs long-term movement using SMA
- Found periods of high volatility through daily returns
- Correlation heatmap revealed strong relationships between price metrics

---

## 🚀 How to Run

1. Clone the repo or download the project folder
2. Make sure Python and Jupyter Notebook are installed
3. Run `nvidia_analysis.ipynb` to see the full analysis in action

---

## ✅ Future Enhancements

- Add stock prediction using LSTM or ARIMA
- Deploy as a Streamlit or Flask dashboard
- Expand to multi-stock comparison

---

## 📬 Contact

Created by **Mratyunjay Saxena** – Feel free to connect on GitHub or LinkedIn for collaborations!
