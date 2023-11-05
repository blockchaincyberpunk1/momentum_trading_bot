import pandas as pd  # Import the pandas library for data handling

def momentum_strategy(historical_data):
    """
    Implement a momentum trading strategy based on moving averages.

    Args:
        historical_data (pandas.DataFrame): DataFrame containing historical price data.

    Returns:
        pandas.DataFrame: DataFrame containing buy signals based on the strategy.
    """
    # Calculate the 50-day and 200-day moving averages and add them as new columns
    historical_data['50MA'] = historical_data['Close'].rolling(window=50).mean()
    historical_data['200MA'] = historical_data['Close'].rolling(window=200).mean()

    # Identify buy signals (Golden Cross: 50-day MA crosses above 200-day MA)
    # Create a boolean mask where the 50-day MA is greater than the 200-day MA
    buy_signals = historical_data[historical_data['50MA'] > historical_data['200MA']]

    return buy_signals  # Return a DataFrame containing buy signals based on the strategy
