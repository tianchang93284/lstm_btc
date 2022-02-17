import asyncio
#import okex.account_api as account
import okex.Account_api as Account
import okex.Funding_api as Funding
import okex.Market_api as Market
import okex.Public_api as Public
import okex.Trade_api as Trade
import okex.subAccount_api as SubAccount
import okex.status_api as Status
import json
import datetime

def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"

time = get_timestamp()

api_key = "97ff9387-7a6d-4c7e-8e2e-7f4e63c2217d"
secret_key = "7268C62AF9C0B103802F93322E84ACDE"
passphrase = "tianchang93824"

marketAPI = Market.MarketAPI(api_key, secret_key, passphrase, False, '0')
result = marketAPI.get_history_candlesticks('BTC-USDT')
print(json.dumps(result))
