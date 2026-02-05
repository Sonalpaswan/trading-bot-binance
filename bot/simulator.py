class TradingSimulator:
    def __init__(self):
        self.orders = []

    def place_market_order(self, symbol, side, quantity):
        order = {
            "orderId": len(self.orders) + 1,
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
            "status": "FILLED"
        }
        self.orders.append(order)
        return order

    def place_limit_order(self, symbol, side, quantity, price):
        order = {
            "orderId": len(self.orders) + 1,
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "price": price,
            "quantity": quantity,
            "status": "OPEN"
        }
        self.orders.append(order)
        return order
