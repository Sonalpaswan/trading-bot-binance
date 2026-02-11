# bot/simulator.py

from bot.storage import load_orders, save_orders


class TradingSimulator:
    def __init__(self):
        self.orders = load_orders()

    def _save(self):
        save_orders(self.orders)

    def place_market_order(self, symbol, side, quantity):
        order = {
            "orderId": len(self.orders) + 1,
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
            "status": "FILLED",
        }
        self.orders.append(order)
        self._save()
        return order

    def place_limit_order(self, symbol, side, quantity, price):
        order = {
            "orderId": len(self.orders) + 1,
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "price": price,
            "quantity": quantity,
            "status": "OPEN",
        }
        self.orders.append(order)
        self._save()
        return order

    def place_stop_limit_order(
        self, symbol, side, quantity, stop_price, limit_price
    ):
        order = {
            "orderId": len(self.orders) + 1,
            "symbol": symbol,
            "side": side,
            "type": "STOP_LIMIT",
            "stopPrice": stop_price,
            "price": limit_price,
            "quantity": quantity,
            "status": "OPEN",
        }
        self.orders.append(order)
        self._save()
        return order
    def cancel_order(self, order_id):
        for order in self.orders:
            if order["orderId"] == order_id:
               if order["status"] != "OPEN":
                   raise Exception("Only OPEN orders can be cancelled")

               order["status"] = "CANCELLED"
               self._save()
               return order

        raise Exception("Order ID not found")

