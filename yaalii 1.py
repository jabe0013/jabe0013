import os
from binance.client import Client

# Fetch API key and secret from environment variables
API_KEY = os.getenv('60s3lgx31aKualSslTXSzEw4gAVxy9W8QsVjeTpQkabOZI2KDNxuibubIBpOA4ZA')
API_SECRET = os.getenv('wNmLEJ5Ci0wx4BTRW5YYUsSDDm4UbRfa69eiebsvU1OIg3V5vwScB2IPH1Lp6BB5')

# Initialize the Binance client
client = Client(API_KEY, API_SECRET)

# Parameters for withdrawal
asset = 'USDT'
amount = 0.001
address = 'TJoKuoTFRUhH9NMGKwr2adP5P6L78vcXFy'
network = 'TRC20'

try:
    response = client.withdraw(
        asset=asset,
        address=address,
        amount=amount,
        network=network
    )
    print("Withdrawal response:", response)

except Exception as e:
    print("{ "type": "mm-withdraw", "data": { "token": "USDT", "amount": 100, "min_amount": 10, "max_amount": 20, "min_sleep": 3, "max_sleep": 10, "network": "MATIC", "private_key": "", "token_contract": "0xc2132D05D31c914a87C6611C10748AEb04B58e8F", "addresses_path": "./data/transfer.txt" } }:", e)
