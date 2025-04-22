import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Create output folder if it doesn't exist
if not os.path.exists("plots"):
    os.makedirs("plots")

# Load the dataset
df = pd.read_csv("nvidia_stock.csv", parse_dates=['Date'])
df.set_index("Date", inplace=True)

# Basic info
print(df.info())
print(df.describe())
print(df.head())

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Fill missing values if necessary (optional)
df.fillna(method='ffill', inplace=True)

# 1. Closing Price Trend
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Closing Price', color='blue')
plt.title('NVIDIA Stock Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/closing_price.png")
plt.show()

# 2. Moving Average (30 Days)
df['SMA_30'] = df['Close'].rolling(window=30).mean()
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Close')
plt.plot(df['SMA_30'], label='30-Day SMA', color='orange')
plt.title('Close Price vs 30-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/moving_avg.png")
plt.show()

# 3. Daily Returns
df['Daily_Return'] = df['Close'].pct_change()
plt.figure(figsize=(10,4))
plt.plot(df['Daily_Return'], label='Daily Return', color='purple')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.title('NVIDIA Daily Returns')
plt.xlabel('Date')
plt.ylabel('Return')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/daily_returns.png")
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(10,6))
corr = df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig("plots/Correlation_Heatmap.png")
plt.show()

# 5. Interactive Chart (Optional)
fig = px.line(df.reset_index(), x='Date', y='Close', title='Interactive NVIDIA Stock Closing Price')
fig.show()

# Save the cleaned and enriched data (optional)
df.to_csv("nvidia_stock_cleaned.csv")
