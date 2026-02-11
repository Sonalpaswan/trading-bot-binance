# 🚀 Binance Futures Trading Bot (Paper Trading Platform)

A professional-grade **paper trading platform** for Binance Futures, built using Python with both **CLI and Web UI** support.

---

## ✨ Key Features
- MARKET, LIMIT & STOP-LIMIT order support
- Command Line Interface (CLI)
- Streamlit-based Web UI
- Persistent order storage (JSON-based)
- Order cancellation support
- Structured logging for debugging & audit
- Modular & extensible backend design

---

## 🔐 Risk-Free Trading & Design Decisions

This project intentionally uses a **paper trading (simulated execution) approach** instead of live Binance trading.

The objective was to:
- Prevent any real financial risk during development and testing
- Ensure safe experimentation with order logic
- Follow responsible engineering practices
- Make the project suitable for internship and academic evaluation

The system is designed so that **real exchange integration can be enabled later** without rewriting core logic.

---

## 🗂 Project Structure
# 🚀 Binance Futures Trading Bot (Paper Trading Platform)

A professional-grade **paper trading platform** for Binance Futures, built using Python with both **CLI and Web UI** support.

---

## ✨ Key Features
- MARKET, LIMIT & STOP-LIMIT order support
- Command Line Interface (CLI)
- Streamlit-based Web UI
- Persistent order storage (JSON-based)
- Order cancellation support
- Structured logging for debugging & audit
- Modular & extensible backend design

---

## 🔐 Risk-Free Trading & Design Decisions

This project intentionally uses a **paper trading (simulated execution) approach** instead of live Binance trading.

The objective was to:
- Prevent any real financial risk during development and testing
- Ensure safe experimentation with order logic
- Follow responsible engineering practices
- Make the project suitable for internship and academic evaluation

The system is designed so that **real exchange integration can be enabled later** without rewriting core logic.

---

## 🗂 Project Structure
trading_bot/
├── bot/
│ ├── cli.py # Command-line interface
│ ├── orders.py # Order execution logic
│ ├── simulator.py # Paper trading engine
│ ├── storage.py # Persistent order storage
│ ├── client.py # Exchange abstraction layer
│ └── logging_config.py # Logging setup
├── ui.py # Streamlit-based web UI
├── orders.json # Stored order data
├── logs.txt # Execution & debug logs
├── requirements.txt
└── README.md