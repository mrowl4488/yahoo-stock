import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for US Stock

symbol = 'AAPL' #Exsample AAPL, NVDA and AMZN
data = yf.download(symbol, start='2020-01-01', end='2025-06-25', interval='1d')


# Function to calculate Average True Range (ATR)
def calculate_atr(df, period=14):
    df['H-L'] = df['High'] - df['Low']
    df['H-PC'] = abs(df['High'] - df['Close'].shift(1))
    df['L-PC'] = abs(df['Low'] - df['Close'].shift(1))
    df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1)
    df['ATR'] = df['TR'].rolling(window=period).mean()
    df['TR/Close'] = df['TR'] / df['Close'].max(axis=1)
    df['ATR%'] = (df['TR/Close'].rolling(window=period).mean())*100
    return df



# Calculate indicators
data_with_atr = calculate_atr(data)
data_with_atr['Value'] = data_with_atr['Volume'] * data_with_atr['Close']
data_with_atr['Value_avg14'] = data_with_atr['Value'].rolling(window=14).mean()


# Plot a new window for index comparison
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True, gridspec_kw={'height_ratios': [1, 1]})

# 1. ATR window
ax1.plot(data_with_atr.index, data_with_atr['ATR%'], label='ATR% (14)', color='green')
ax1.set_title('ATR% (14) - Average True Range%')
ax1.set_ylabel('ATR%')
ax1.legend()

# 2. Value window (14-day avg for smoother chart)
ax2.plot(data_with_atr.index, data_with_atr['Value_avg14'], label='Value (14-day Avg)', color='blue')
ax2.set_title('Trading Value (Volume × Close, 14-day Avg)')
ax2.set_ylabel('Value (USD)')
ax2.legend()


plt.tight_layout()
plt.show()
#data.to_csv(r'C:/Users/Admin/Desktop/Coder/AAPL_data.csv') #Save csv to desktop #you can delete "#" to save csv file. ลบ "#" ข้างหน้าบรรทัดจะเชฟไฟล์ CSV ได้
