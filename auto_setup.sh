#!/bin/bash

echo "🔄 Checking Alchemy API Key..."

# Check if ALCHEMY_API_KEY is set
if [ -z "$ALCHEMY_API_KEY" ] || [ "$ALCHEMY_API_KEY" == "your_actual_alchemy_api_key" ]; then
    echo "⚠️ API key is missing or incorrect! Setting the correct key now..."
    
    # Set the correct API key
    export ALCHEMY_API_KEY="mUfUQOUWNLa-jXgzBeP42JywB87alznt"
    echo 'export ALCHEMY_API_KEY="mUfUQOUWNLa-jXgzBeP42JywB87alznt"' >> ~/.zshrc
    source ~/.zshrc
fi

# Verify the API Key
echo "✅ Verifying API Key..."
response=$(curl -s -X POST -H "Content-Type: application/json" \
    --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' \
    https://eth-mainnet.g.alchemy.com/v2/$ALCHEMY_API_KEY)

if echo "$response" | grep -q "result"; then
    echo "🎉 API Key is valid!"
else
    echo "❌ API Key is still invalid! Please check your Alchemy dashboard."
    exit 1
fi

# Run Nova Transaction Script
echo "🚀 Starting Nova Auto Transaction Script..."
nohup python3 nova_auto_transaction.py > nova_tx_log.txt 2>&1 &
disown
echo "✅ Nova is now running in the background!"
