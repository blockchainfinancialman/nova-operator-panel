import os
import time
from web3 import Web3

# Load API keys securely
alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/" + os.getenv("ALCHEMY_API_KEY")
private_key = os.getenv("WALLET_PRIVATE_KEY").strip()
sender = "0xE51Dce59b42f008dB7A3Ef29d43bC712A56B99B9"  # Replace with your wallet address
recipient = "0xccA9341830fa27f44ED1Ed3D259851D449bdfA59"  # Replace with recipient's address

# Connect to Ethereum
web3 = Web3(Web3.HTTPProvider(alchemy_url))

def send_eth():
    if not web3.is_connected():
        print("⚠️ Connection failed. Retrying in 5 minutes...")
        return

    # Check sender's ETH balance
    balance = web3.eth.get_balance(sender)
    eth_balance = web3.from_wei(balance, 'ether')
    print(f"💰 Balance: {eth_balance} ETH")

    if eth_balance < 0.02:  # Ensure there's enough ETH for gas & transaction
        print("⚠️ Insufficient funds. Skipping transaction.")
        return

    try:
        # Create transaction
        txn = {
            "to": recipient,
            "value": web3.to_wei(0.01, "ether"),  # Sending 0.01 ETH
            "gas": 21000,
            "gasPrice": web3.to_wei("50", "gwei"),
            "nonce": web3.eth.get_transaction_count(sender),
        }

        # Sign & send transaction
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"✅ Transaction Sent! Tx Hash: {web3.to_hex(tx_hash)}")

    except Exception as e:
        print(f"❌ Error: {str(e)}. Retrying in 5 minutes.")

# **Continuous Execution Loop**
while True:
    send_eth()
    time.sleep(1800)  # Run every 30 minutesmport os
from web3 import Web3

# Load API keys
alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/" + os.getenv("ALCHEMY_API_KEY")
private_key = os.getenv("WALLET_PRIVATE_KEY")  # Securely load your private key

# Define Wallet Addresses
sender = "0xYourSenderAddress"  # Replace with your wallet address
recipient = "0xYourRecipientAddress"  # Replace with your recipient's address

# Connect to Ethereum via Alchemy
web3 = Web3(Web3.HTTPProvider(alchemy_url))

if web3.is_connected():
    print("✅ Connected to Ethereum via Alchemy API")

    # Check Sender's Balance
    balance = web3.eth.get_balance(sender)
    eth_balance = web3.from_wei(balance, 'ether')
    print(f"💰 Balance: {eth_balance} ETH")

    if eth_balance < 0.02:  # Ensure there's enough ETH for gas & transaction
        print("⚠️ Insufficient funds to send 0.01 ETH!")
    else:
        # Create Transaction
        txn = {
            "to": recipient,
            "value": web3.to_wei(0.01, "ether"),  # Send 0.01 ETH
            "gas": 21000,
            "gasPrice": web3.to_wei("50", "gwei"),
            "nonce": web3.eth.get_transaction_count(sender),
        }

        # Sign and Send Transaction
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
        print(f"Signed Transaction Object: {signed_txn}")
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

        print(f"✅ Transaction Sent! Tx Hash: {web3.to_hex(tx_hash)}")

else:
    print("⚠️ Connection failed. Check API key or network URL.")

