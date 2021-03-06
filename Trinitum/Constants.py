
NOT_SET = None
CURRENT_TICK_HOLD = "NO POSITION/HOLD POSITION"
NO_EXIT_POSITIONS = "IN POSITION/NO EXIT POSITIONS"

GDAX_TICKERS = ['BTC-USD', 'LTC-USD', 'ETH-USD']
POLONIEX_TICKERS = ["USDT_BTC", "USDT_LTC", "USDT_ETH", "USDT_ETC"]
GDAX_TO_POLONIEX = {'BTC-USD': "USDT_BTC", 'LTC-USD': "USDT_LTC", 'ETH-USD': "USDT_ETC"}
POLO_PUBLIC_API = (0,0)

DAILY_RISK_FREE_RATE =  ((1+.91/100)**(1/252)-1)

SOFT_EXIT, HARD_EXIT = 0, 1
BUY_SIGNAL, SELL_SIGNAL = 1, -1
READ_PRIORITY, WRITE_PRIORITY = 2, 3

GDAX_FUNDS_ERROR = {'message': 'Insufficient funds'}

DEFAULT_QUANTITY, DEFAULT_RISK_TOL, DEFAULT_POS_LIMIT = .01, .05, 1
DEFAULT_IND_LAG, DEFAULT_SYS_LAG = 1, 0
DEFAULT_CUSTOM_LOGIC, DEFAULT_CUSTOM_DATA = None, {}

DEFAULT_RISK_PARAMETERS = {
"posLimit": DEFAULT_POS_LIMIT, 
"tolerance": DEFAULT_RISK_TOL
}

DEFAULT_SPOT_DATA_DICT = {
'price': None,
'volume': None,
'bid': None,
'ask': None
}

DEFAULT_CAPITAL_DICT = {
'capital' : None,
'commission' : None, 
'returns' : None
}


