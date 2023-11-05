if __name__ == "__main__":
    # Import required libraries and modules
    from decouple import config  # For reading API keys from .env
    import pandas as pd  # For data manipulation
    from strategies.momentum_strategy import momentum_strategy  # Import the momentum strategy
    from utils.ib_api_utils import execute_trades  # Import the execute_trades function

    # Load API keys from .env
    ib_api_key = config("IB_API_KEY")  # Get Interactive Brokers API key from .env
    yahoo_finance_api_key = config("YAHOO_FINANCE_API_KEY")  # Get Yahoo Finance API key from .env

    # Fetch historical data using yfinance
    import yfinance as yf  # Import the yfinance library
    symbol = "AAPL"  # Define the asset symbol (e.g., AAPL for Apple Inc.) - Change to your desired symbol
    start_date = "2022-01-01"  # Define the start date for historical data
    end_date = "2023-01-01"  # Define the end date for historical data

    # Use yfinance to download historical price data for the specified asset and date range
    historical_data = yf.download(symbol, start=start_date, end=end_date)

    # Implement and apply your momentum trading strategy
    buy_signals = momentum_strategy(historical_data)  # Generate buy signals based on the strategy

    # Execute trades using Interactive Brokers
    execute_trades(ib_api_key, buy_signals)  # Execute buy orders based on buy signals

""" 
The script is designed to run when executed directly (not imported as a module) by checking if __name__ == "__main__":.
Import the necessary libraries, modules, and functions required for the trading bot, including reading API keys, data manipulation, the momentum strategy, and executing trades.
API keys are loaded securely from the .env file using the config function from the decouple library.
Historical price data is fetched using the yfinance library for a specified asset symbol, start date, and end date.
The momentum strategy is applied to the historical data, generating buy signals based on the strategy.
Finally, the execute_trades function is called to execute buy orders using the Interactive Brokers API based on the generated buy signals.

"""