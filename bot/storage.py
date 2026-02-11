# bot/storage.py

import json
import os

ORDERS_FILE = "orders.json"


def load_orders():
    if not os.path.exists(ORDERS_FILE):
        return []

    try:
        with open(ORDERS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_orders(orders):
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=4)
