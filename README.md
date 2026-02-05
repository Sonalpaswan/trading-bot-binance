# Trading Bot using Binance API

## Description
This project implements a CLI-based trading bot using Binance API.
It supports MARKET and LIMIT orders and includes a simulator for safe testing.

## Features
- Place MARKET orders
- Place LIMIT orders
- Trading simulator (no real money risk)
- Logging of orders and errors
- Secure API key handling via environment variables

## Project Structure
trading_bot/
├── bot/
│   ├── cli.py
│   ├── orders.py
│   ├── simulator.py
│   ├── client.py
│   ├── logging_config.py
├── requirements.txt
├── README.md

## Setup Instructions
1. Clone the repository
2. Create virtual environment
3. Install dependencies:
   pip install -r requirements.txt

## How to Run

### Market Order
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000

## Assumptions
- Simulator is used to avoid real financial risk
- API keys are not committed for security reasons
Note: This is a CLI-based project. A UI was optional as per assignment and not implemented.
