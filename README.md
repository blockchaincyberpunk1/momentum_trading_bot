# Momentum Trading Bot

  [![License](https://img.shields.io/static/v1?label=License&message=MIT&color=blue&?style=plastic&logo=appveyor)](https://opensource.org/license/MIT)



## Table Of Content

- [Description](#description)
- [Deployed website link](#deployedWebsite)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contribution)
- [Tests](#tests)
- [GitHub](#github)
- [Contact](#contact)
- [License](#license)




![GitHub repo size](https://img.shields.io/github/repo-size/blockchaincyberpunk1/momentum_trading_bot?style=plastic)

  ![GitHub top language](https://img.shields.io/github/languages/top/blockchaincyberpunk1/momentum_trading_bot?style=plastic)



## Description

  The Momentum Trading Bot is a Python-based bot that identifies and trades assets with strong price momentum. It uses Pandas and NumPy for data analysis, the Interactive Brokers API for trading, and Yahoo Finance for historical data. API keys are securely stored in a .env file.





<p align="center">
  <img alt="Momentum Trading Bot" [Screenshot] src="python-trading-bot.jpg"><br>
Momentum Trading Bot
</p>





## Installation

1. Clone the Repository

git clone https://github.com/blockchaincyberpunk1/momentum_trading_bot.git
cd momentum_trading_bot

2. Create a Virtual Environment (Optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. Install Required Libraries

pip install -r requirements.txt

4. Secure Your API Keys

Create a .env file in the project directory and add your API keys as follows:

IB_API_KEY=your_ib_api_key
YAHOO_FINANCE_API_KEY=your_yahoo_finance_api_key

5. Fetch Historical Data

Create a function to fetch historical data using Yahoo Finance and save it to data/historical_data.csv. Adapt and include this function in your code.

6. Implement Momentum Strategy

Create and implement a momentum trading strategy in strategies/momentum_strategy.py.

7. Interactive Brokers Integration

Use the ib_insync library to interact with the Interactive Brokers API. Include this functionality in utils/ib_api_utils.py.

8. Run the Bot

In main.py, include the main logic for your trading bot. Fetch historical data, apply the momentum strategy, and execute trades.

python main.py




Momentum Trading Bot is built with the following tools and libraries: <ul><li>Interactive Brokers API: Allows for real-time trading and interaction with financial markets.</li> <li>Yahoo Finance API: Used to fetch historical price data for various assets.</li> <li>Python-decouple: Used to securely store and retrieve API keys from a .env file.</li> <li>ib-insync: A Python library for interactive trading with Interactive Brokers.</li></ul>





## Usage
 
Run the bot using the provided instructions. It will identify assets with strong price momentum and execute trades accordingly.




## Contribution
 
Contributions to this project are welcome! If you would like to contribute, feel free to open issues, submit pull requests, or make suggestions for improvements.





## Tests
 
Test the bot's functionality by running it with historical data and verifying that it correctly identifies and trades assets with strong momentum.




## GitHub

<a href="https://github.com/blockchaincyberpunk1"><strong>blockchaincyberpunk1</a></strong>



<p>Visit my website: <strong><a href="http://blockchaincyberpunk1.github.io/thepolyglot">The Polyglot</a></strong></p>





## Contact

Feel free to reach out to me on my email:
thepolyglot8@gmail.com





## License

[![License](https://img.shields.io/static/v1?label=Licence&message=MIT&color=blue)](https://opensource.org/license/MIT)


