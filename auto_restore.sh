#!/bin/bash

# Define file path
NOVA_SCRIPT=~/nova-operator-mode/nova_trader.py

# Ensure the directory exists
mkdir -p ~/nova-operator-mode

# Check if nova_trader.py exists
if [ ! -f "$NOVA_SCRIPT" ]; then
    echo "nova_trader.py is missing! Restoring..."
    
    # Recreate nova_trader.py
    cat <<EOL > "$NOVA_SCRIPT"
print("Nova Trader has started successfully!")
import time

while True:
    print("Nova is running...")
    time.sleep(5)
EOL

    chmod +x "$NOVA_SCRIPT"
    echo "nova_trader.py restored!"
fi

# Run nova_trader.py in the background and disown it
nohup python3 "$NOVA_SCRIPT" > /dev/null 2>&1 &
disown

echo "Nova Trader is running!"
