{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOrh0yuWg7K06YeWT9zBh9W"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"id":"pKPvhoR_tEfd"},"outputs":[],"source":["import pandas as pd\n","import requests\n","\n","class TradingAgent:\n","    \"\"\"Base class for trading agents.\"\"\"\n","    def __init__(self, initial_cash=100000):\n","        self.initial_cash = initial_cash\n","        self.cash = initial_cash\n","        self.position = 0  # Number of units of the asset\n","        self.history = []  # To store trade history\n","\n","    def generate_signals(self, data):\n","        \"\"\"Generate trading signals. To be implemented by subclasses.\"\"\"\n","        raise NotImplementedError\n","\n","    def trade(self, price, signal):\n","        \"\"\"Execute trades based on the signal.\"\"\"\n","        if signal == 1:  # Buy\n","            self.position += self.cash / price\n","            self.cash = 0\n","            self.history.append(f\"Buy at {price}\")\n","        elif signal == -1:  # Sell\n","            self.cash += self.position * price\n","            self.position = 0\n","            self.history.append(f\"Sell at {price}\")\n","        # Hold: Do nothing\n","        self.history.append(f\"Hold at {price}\")\n","\n","    def get_portfolio_value(self, price):\n","        \"\"\"Calculate total portfolio value.\"\"\"\n","        return self.cash + (self.position * price)\n","\n","def fetch_historical_data(symbol, interval, limit=1000):\n","    \"\"\"Fetch historical data from Binance API.\"\"\"\n","    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'\n","    response = requests.get(url)\n","    data = response.json()\n","    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',\n","                                     'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',\n","                                     'taker_buy_quote_asset_volume', 'ignore'])\n","    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')\n","    df.set_index('timestamp', inplace=True)\n","    df = df[['open', 'high', 'low', 'close', 'volume']].astype(float)\n","    return df\n","\n","def calculate_performance_metrics(initial_cash, final_value):\n","    \"\"\"Calculate performance metrics.\"\"\"\n","    total_return = (final_value - initial_cash) / initial_cash\n","    return {\"Total Return\": total_return}"]}]}