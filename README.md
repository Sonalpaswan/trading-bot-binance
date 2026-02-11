# 🚀 Binance Futures Trading Bot (Paper Trading Platform)

A professional-grade **paper trading platform** for Binance Futures, developed using **Python**, supporting both a **Command Line Interface (CLI)** and a **Web-based UI (Streamlit)**.

This project demonstrates clean architecture, modular backend design, and safe trading logic suitable for academic and internship evaluation.

---

## ✨ Key Features

- Supports **MARKET**, **LIMIT**, and **STOP-LIMIT** orders  
- Command Line Interface (CLI) for fast execution  
- Streamlit-based Web UI for interactive order placement  
- Persistent order storage using JSON  
- Order cancellation support  
- Structured logging for debugging and audit  
- Modular, extensible backend architecture  

---

## 🔐 Risk-Free Trading & Engineering Decisions

This project intentionally follows a **paper trading (simulated execution)** approach instead of live Binance trading.

### Why paper trading?
- To **eliminate real financial risk** during development and testing  
- To allow **safe experimentation** with trading logic  
- To follow **responsible software engineering practices**  
- To make the project suitable for **internship and academic submission**

⚠️ **Important Note:**  
The architecture is designed in a way that **real Binance Futures API integration can be enabled later** with minimal changes, without rewriting the core business logic.

---

## 🗂 Project Structure

trading_bot/
│
├── bot/
│   ├── cli.py              # Command-line interface
│   ├── orders.py           # Order execution logic
│   ├── simulator.py        # Paper trading engine
│   ├── storage.py          # Persistent order storage
│   ├── client.py           # Exchange abstraction layer
│   └── logging_config.py   # Logging configuration
│
├── ui.py                   # Streamlit-based web UI
├── orders.json             # Stored order data
├── logs.txt                # Execution and debug logs
├── requirements.txt
└── README.md
