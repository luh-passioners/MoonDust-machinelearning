import yfinance as yf
import numpy as np
from IBD50_Tickers import get_tickers

def __init__(self):
    # Call get_tickers from Class1 to get the list of tickers
    self.stock_tickers = get_tickers()

stock_tickers = get_tickers()

def calculate_current_price(ticker_symbol):
    """
    Calculate the current price for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
    
    Returns:
        current_price (float): Current price of the stock.
    """
    # Fetch current price
    stock_data = yf.Ticker(ticker_symbol)
    current_price = stock_data.history(period="1d")["Close"].iloc[-1]
    
    return round(current_price, 2)

def get_20_day_sma(ticker_symbol):
    """
    Calculate the 20-day Simple Moving Average (SMA) for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
    
    Returns:
        sma_20 (float): 20-day SMA of the stock.
    """
    # Create a Ticker object
    stock_data = yf.Ticker(ticker_symbol)
    
    # Fetch historical data for SMA calculation
    historical_data = stock_data.history(period="21d")  # Fetch 21 days to include current day
    
    # Check if there is enough data for SMA calculation
    if len(historical_data) < 21:
        return 0
    
    # Calculate SMA
    sma_20 = historical_data["Close"].mean()
    
    if isinstance(sma_20, np.float64):
        return round(sma_20, 2)
    else:
        return round(sma_20.iloc[-1], 2)

def get_50_day_sma(ticker_symbol):
    """
    Calculate the 50-day Simple Moving Average (SMA) for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
    
    Returns:
        sma_50 (float): 50-day SMA of the stock.
    """
    # Create a Ticker object
    stock_data = yf.Ticker(ticker_symbol)
    
    # Fetch historical data for SMA calculation
    historical_data = stock_data.history(period="51d")  # Fetch 51 days to include current day
    
    # Check if there is enough data for SMA calculation
    if len(historical_data) < 51:
        return 0
    
    # Calculate SMA
    sma_50 = historical_data["Close"].mean()
    
    if isinstance(sma_50, np.float64):
        return round(sma_50, 2)
    else:
        return round(sma_50.iloc[-1], 2)



def get_sales_last_quarter(ticker_symbol):
    """
    Get the Sales % last quarter for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
    
    Returns:
        sales_last_qtr (float): Sales % last quarter.
    """
    # Fetch company data
    stock_data = yf.Ticker(ticker_symbol)
    company_info = stock_data.info
    
    # Get Sales % last quarter
    sales_last_qtr = company_info.get("quarterlyRevenueGrowth", "N/A")
    
    if isinstance(sales_last_qtr, str) and sales_last_qtr != "N/A":
        # Convert the string to a numeric value
        sales_last_qtr = float(sales_last_qtr.strip('%'))
    
    return round(sales_last_qtr, 2) if isinstance(sales_last_qtr, float) else 0  # Return 0 if sales_last_qtr is None or not a float



def get_roe(ticker_symbol):
    """
    Get the Return on Equity (ROE) for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
    
    Returns:
        roe (float): Return on Equity (ROE).
    """
    # Fetch company data
    stock_data = yf.Ticker(ticker_symbol)
    company_info = stock_data.info
    
    # Get ROE
    roe = company_info.get("returnOnEquity", "N/A")
    
    if isinstance(roe, str) and roe == "N/A":
        return 0
    else:
        return round(float(roe), 2)


def get_profit_margin(ticker_symbol):
    """
    Get the Profit Margin for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
    
    Returns:
        profit_margin (float): Profit Margin.
    """
    # Fetch company data
    stock_data = yf.Ticker(ticker_symbol)
    company_info = stock_data.info
    
    # Get Profit Margin
    profit_margin = company_info.get("profitMargins", "N/A")
    
    if isinstance(profit_margin, str) and profit_margin == "N/A":
        return 0
    else:
        return round(float(profit_margin) * 100, 2)


def get_pe_ratio(ticker_symbol):
    """
    Get the Price-to-Earnings (P/E) ratio for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
    
    Returns:
        pe_ratio (float): Price-to-Earnings (P/E) ratio.
    """
    # Fetch company data
    stock_data = yf.Ticker(ticker_symbol)
    company_info = stock_data.info
    
    # Get P/E ratio
    pe_ratio = company_info.get("trailingPE", "N/A")
    
    if isinstance(pe_ratio, str) and pe_ratio == "N/A":
        return 0
    else:
        return round(float(pe_ratio), 2)


def get_eps(ticker_symbol):
    """
    Get the Earnings Per Share (EPS) for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
    
    Returns:
        eps (float): Earnings Per Share (EPS).
    """
    # Fetch company data
    stock_data = yf.Ticker(ticker_symbol)
    company_info = stock_data.info
    
    # Get EPS
    eps = company_info.get("trailingEps", "N/A")
    
    if isinstance(eps, str) and eps == "N/A":
        return 0
    else:
        return round(float(eps), 2)


def get_rsi(ticker_symbol, period=14):
    """
    Calculate the Relative Strength Index (RSI) for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
        period (int): The period for RSI calculation (default is 14).
    
    Returns:
        rsi (float): The Relative Strength Index.
    """
    # Fetch historical data
    stock_data = yf.Ticker(ticker_symbol)
    historical_data = stock_data.history(period=f"{period+1}d")
    
    if len(historical_data) <= period:
        return 0
    
    # Calculate price changes
    delta = historical_data['Close'].diff(1)
    
    # Calculate gains and losses
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    # Calculate Relative Strength
    rs = gain / loss
    
    # Calculate RSI
    rsi = 100 - (100 / (1 + rs.iloc[-1]))
    
    return rsi

def is_price_between_bollinger_bands(ticker_symbol, period=20, std_dev=2):
    """
    Check if the price is between the lower and higher Bollinger Bands for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
        period (int): The period for Bollinger Bands calculation (default is 20).
        std_dev (int): The standard deviation multiplier for Bollinger Bands (default is 2).
    
    Returns:
        bool: True if the price is between the lower and higher Bollinger Bands, False otherwise.
    """
    # Fetch historical data
    stock_data = yf.Ticker(ticker_symbol)
    historical_data = stock_data.history(period=f"{period+1}d")
    
    if len(historical_data) < period + 1:
        return False
    
    # Calculate the middle band (simple moving average)
    middle_band = historical_data['Close'].rolling(window=period).mean()
    
    # Calculate the standard deviation
    std = historical_data['Close'].rolling(window=period).std()
    
    # Calculate the upper and lower bands
    upper_band = middle_band + std_dev * std
    lower_band = middle_band - std_dev * std
    
    # Check if the current price is between the lower and higher bands
    current_price = historical_data['Close'].iloc[-1]
    return lower_band.iloc[-1] < current_price < upper_band.iloc[-1]

def calculate_stochastic_oscillator(ticker_symbol, period=14, smoothing=3):
    """
    Calculate the Stochastic Oscillator for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
        period (int): The period for Stochastic Oscillator calculation (default is 14).
        smoothing (int): The smoothing factor for %D line (default is 3).
    
    Returns:
        float: The current value of the Stochastic Oscillator.
    """
    try:
        # Fetch historical data
        stock_data = yf.Ticker(ticker_symbol)
        historical_data = stock_data.history(period=f"{period+smoothing}d")
        
        if len(historical_data) < period + smoothing:
            return 0
        
        # Calculate %K line
        low_min = historical_data['Low'].rolling(window=period).min()
        high_max = historical_data['High'].rolling(window=period).max()
        K_line = 100 * (historical_data['Close'] - low_min) / (high_max - low_min)
        
        # Calculate %D line (smoothing)
        D_line = K_line.rolling(window=smoothing).mean()
        
        # Get the current value of %D line
        current_stochastic_oscillator = D_line.iloc[-1]
        
        return current_stochastic_oscillator
    except Exception as e:
        print(f"Error calculating Stochastic Oscillator for {ticker_symbol}: {e}")
        return 0




# printing stock info used towards testing. 
def print_stock_info(ticker_symbol):
    """
    Print financial metrics for a given stock ticker symbol.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the stock.
    """
    # Fetch current price
    current_price = calculate_current_price(ticker_symbol)
    
    # Print results
    print("Ticker:", ticker_symbol)
    print("Current Price:", current_price)
    print("20-Day SMA:", get_20_day_sma(ticker_symbol))
    print("50-Day SMA:", get_50_day_sma(ticker_symbol))
    print("Sales % Last Quarter:", get_sales_last_quarter(ticker_symbol))
    print("ROE:", get_roe(ticker_symbol))
    print("Profit Margin:", get_profit_margin(ticker_symbol))
    print("P/E Ratio:", get_pe_ratio(ticker_symbol))
    print("EPS:", get_eps(ticker_symbol))
    print("RSI", get_rsi(ticker_symbol))
    print("In between Bollinger Bands?", is_price_between_bollinger_bands(ticker_symbol))
    print("Stochastic Oscillator", calculate_stochastic_oscillator(ticker_symbol))
    print("\n")



# Initialize a dictionary to store stock scores
stock_scores = {}

# Iterate through each ticker and calculate score
for ticker_symbol in stock_tickers:
    fundamentalScore = 0
    technicalScore = 0

    if calculate_current_price(ticker_symbol) > get_20_day_sma(ticker_symbol):
        technicalScore += 1
    
    if calculate_current_price(ticker_symbol) > get_50_day_sma(ticker_symbol):
        technicalScore += 1
    
    if get_sales_last_quarter(ticker_symbol) > 0:
        fundamentalScore += 1
    
    if get_roe(ticker_symbol) > 5:
        fundamentalScore += 1
    
    if get_profit_margin(ticker_symbol) > 0:
        fundamentalScore += 1
    
    if get_pe_ratio(ticker_symbol) > 0:
        fundamentalScore += 1
    
    if get_eps(ticker_symbol) > 0:
        fundamentalScore += 1
    
    if 30 < get_rsi(ticker_symbol) < 70:
        technicalScore += 1
    
    if is_price_between_bollinger_bands(ticker_symbol):
        technicalScore += 1
    
    if 20 < calculate_stochastic_oscillator(ticker_symbol) < 80:
        technicalScore += 1
    
    # Assign the scores to the ticker symbol
    stock_scores[ticker_symbol] = {
        'Technical Score': technicalScore,
        'Fundamental Score': fundamentalScore
    }

# Sort the stock_scores dictionary by fundamental score in descending order
sorted_fundamental_scores = sorted(stock_scores.items(), key=lambda x: x[1]['Fundamental Score'], reverse=True)

# Print the sorted stock scores by fundamental score
print("Sorted Stock Scores by Fundamental Score:")
for ticker_symbol, scores in sorted_fundamental_scores:
    print(ticker_symbol, ":", (scores['Fundamental Score'] - 2.5) / 2.5)

# Sort the stock_scores dictionary by technical score in descending order
sorted_technical_scores = sorted(stock_scores.items(), key=lambda x: x[1]['Technical Score'], reverse=True)

# Print the sorted stock scores by technical score
print("\nSorted Stock Scores by Technical Score:")
for ticker_symbol, scores in sorted_technical_scores:
    print(ticker_symbol, ":", (scores['Technical Score'] - 2.5) / 2.5)