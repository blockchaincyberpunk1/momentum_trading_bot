from ib_insync import IB, util  # Import the necessary modules from ib_insync
from decouple import config  # Import the decouple library for reading API keys from .env file

def execute_trades(ib_api_key, buy_signals):
    """
    Execute buy orders for assets based on buy signals using the Interactive Brokers API.

    Args:
        ib_api_key (str): The Interactive Brokers API key for authentication.
        buy_signals (pandas.DataFrame): DataFrame containing buy signals.

    Returns:
        None
    """
    # Connect to the Interactive Brokers API
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)  # Connect to the local Interactive Brokers TWS/Gateway

    try:
        # Place buy orders based on buy signals
        for symbol in buy_signals['Symbol']:
            # Qualify the contract for the asset
            contract = ib.qualifyContracts(ib.contract(symbol, 'STK', 'SMART', 'USD'))
            
            # Place a market order to buy 100 shares of the asset
            order = ib.placeOrder(contract[0], ib.Order('MKT', 100))
            
            # Sleep for 2 seconds between orders (rate limiting)
            ib.sleep(2)

        # Disconnect from the Interactive Brokers API
        ib.disconnect()

    except Exception as e:
        print(f"Error executing trades: {e}")
        ib.disconnect()  # Disconnect from Interactive Brokers in case of an error or after execution
