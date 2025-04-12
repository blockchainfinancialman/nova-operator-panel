import os
from web3 import Web3

# Load API keys from environment variables
alchemy_url = f"https://eth-mainnet.alchemyapi.io/v2/{os.getenv('ALCHEMY_API_KEY')}"

# Connect to Ethereum via Alchemy
web3 = Web3(Web3.HTTPProvider(alchemy_url))

if web3.is_connected():
    print("✅ Connected to Ethereum via Alchemy API")
else:
    print("⚠️ Connection failed. Check API key.")
