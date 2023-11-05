import pandas as pd  # Import the pandas library for data handling

def fetch_historical_data(symbol, start_date, end_date):
    """
    Fetch historical price data for a given asset symbol within a specified date range.

    Args:
        symbol (str): The symbol of the asset you want to fetch data for (e.g., AAPL for Apple Inc.).
        start_date (str): The start date in the format 'YYYY-MM-DD' for the historical data.
        end_date (str): The end date in the format 'YYYY-MM-DD' for the historical data.

    Returns:
        pandas.DataFrame: A DataFrame containing the historical price data.
    """
    # Use yfinance to fetch historical data for the specified asset symbol
    import yfinance as yf
    historical_data = yf.download(symbol, start=start_date, end=end_date)

    # Save the fetched historical data to a CSV file in the 'data/' directory
    historical_data.to_csv(f'data/historical_data_{symbol}.csv')

    return historical_data  # Return the DataFrame containing the historical price data
