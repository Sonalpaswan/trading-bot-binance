from bot.simulator import TradingSimulator

from .logging_config import setup_logger

logger = setup_logger()
simulator = TradingSimulator()


def place_market_order(symbol, side, quantity):
    logger.info("Placing MARKET order")
    order = simulator.place_market_order(symbol, side, quantity)
    logger.info(f"Order executed: {order}")
    return order


def place_limit_order(symbol, side, quantity, price):
    logger.info("Placing LIMIT order")
    order = simulator.place_limit_order(symbol, side, quantity, price)
    logger.info(f"Order placed: {order}")
    return order

def place_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    logger.info("Placing STOP-LIMIT order")

    order = simulator.place_stop_limit_order(
        symbol=symbol,
        side=side,
        quantity=quantity,
        stop_price=stop_price,
        limit_price=limit_price
    )

    logger.info(f"STOP-LIMIT order placed: {order}")
    return order
def cancel_order(order_id):
    logger.info(f"Cancelling order ID {order_id}")
    order = simulator.cancel_order(order_id)
    logger.info(f"Order cancelled: {order}")
    return order

