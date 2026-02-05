from .simulator import TradingSimulator
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
