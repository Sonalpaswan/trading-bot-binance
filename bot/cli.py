import argparse
from bot.orders import place_market_order, place_limit_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True)
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    if args.type == "LIMIT" and args.price is None:
        parser.error("LIMIT order requires --price")

    try:
        if args.type == "MARKET":
            order = place_market_order(
                args.symbol, args.side, args.quantity
            )
        else:
            order = place_limit_order(
                args.symbol, args.side, args.quantity, args.price
            )

        print("\n✅ Order placed successfully")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice", "N/A"))

    except Exception as e:
        print("\n❌ Order failed")
        print("Error:", e)

if __name__ == "__main__":
    main()
