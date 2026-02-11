import argparse

from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order,
    cancel_order
)

from bot.storage import load_orders


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot (Simulator)"
    )

    # ===== Global actions =====
    parser.add_argument(
        "--show-orders",
        action="store_true",
        help="Show all stored orders"
    )

    parser.add_argument(
        "--cancel",
        type=int,
        help="Cancel order by Order ID"
    )

    # ===== Order arguments =====
    parser.add_argument("--symbol", help="Trading pair (e.g. BTCUSDT)")
    parser.add_argument("--side", choices=["BUY", "SELL"], help="Order side")
    parser.add_argument(
        "--type",
        choices=["MARKET", "LIMIT", "STOP_LIMIT"],
        help="Order type"
    )
    parser.add_argument("--quantity", type=float, help="Order quantity")

    # ===== Price arguments =====
    parser.add_argument("--price", type=float, help="Limit price")
    parser.add_argument("--stop_price", type=float, help="Stop price (STOP_LIMIT)")

    args = parser.parse_args()

    # ===== SHOW ORDERS =====
    if args.show_orders:
        orders = load_orders()
        if not orders:
            print("📭 No orders found")
        else:
            print("\n📦 Order History:")
            for o in orders:
                print(o)
        return

    # ===== CANCEL ORDER =====
    if args.cancel is not None:
        try:
            order = cancel_order(args.cancel)
            print("\n✅ Order cancelled successfully")
            print("Order ID:", order.get("orderId"))
            print("Status:", order.get("status"))
        except Exception as e:
            print("\n❌ Cancel failed")
            print("Error:", e)
        return

    # ===== VALIDATION FOR ORDER PLACEMENT =====
    if not args.symbol or not args.side or not args.type or not args.quantity:
        parser.error(
            "Order placement requires --symbol --side --type --quantity"
        )

    if args.type == "LIMIT" and args.price is None:
        parser.error("LIMIT order requires --price")

    if args.type == "STOP_LIMIT":
        if args.price is None or args.stop_price is None:
            parser.error("STOP_LIMIT order requires --price and --stop_price")

    try:
        # ===== EXECUTION =====
        if args.type == "MARKET":
            order = place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )

        elif args.type == "LIMIT":
            order = place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        elif args.type == "STOP_LIMIT":
            order = place_stop_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.stop_price,
                args.price
            )

        # ===== OUTPUT =====
        print("\n✅ Order placed successfully")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty", "N/A"))
        print("Avg Price:", order.get("avgPrice", "N/A"))

    except Exception as e:
        print("\n❌ Order failed")
        print("Error:", e)


if __name__ == "__main__":
    main()
