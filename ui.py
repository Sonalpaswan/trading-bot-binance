import streamlit as st
import streamlit as st

st.set_page_config(
    page_title="Binance Futures Trading Bot",
    layout="centered"
)

st.title("📈 Binance Futures Trading Bot")
st.caption(
    "A professional paper-trading platform supporting MARKET, LIMIT & STOP-LIMIT orders. "
    "Built using Python, Streamlit and a modular backend architecture."
)


st.divider()


from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order,
    cancel_order
)

from bot.storage import load_orders

st.set_page_config(page_title="Trading Bot UI", layout="wide")
st.title("📊 Binance Futures Trading Bot (Simulator)")

tab1, tab2 = st.tabs(["➕ Place Order", "📦 Order History"])

# ================= PLACE ORDER =================
with tab1:
    symbol = st.text_input("Symbol", "BTCUSDT")
    side = st.selectbox("Side", ["BUY", "SELL"])
    order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP_LIMIT"])
    quantity = st.number_input("Quantity", min_value=0.001, step=0.001)

    price = None
    stop_price = None

    if order_type in ["LIMIT", "STOP_LIMIT"]:
        price = st.number_input("Price", min_value=0.0)

    if order_type == "STOP_LIMIT":
        stop_price = st.number_input("Stop Price", min_value=0.0)

    if st.button("🚀 Place Order"):
     if st.button("🚀 Place Order"):
        

    # ===== VALIDATION =====
      if quantity <= 0:
        st.warning("⚠ Quantity must be greater than 0")
        st.stop()

    if order_type in ["LIMIT", "STOP_LIMIT"] and price is None:
        st.warning("⚠ Price is required for LIMIT / STOP_LIMIT orders")
        st.stop()

    if order_type in ["LIMIT", "STOP_LIMIT"] and price <= 0:
        st.warning("⚠ Price must be greater than 0")
        st.stop()

    if order_type == "STOP_LIMIT" and stop_price is None:
        st.warning("⚠ Stop Price is required for STOP_LIMIT orders")
        st.stop()

    if order_type == "STOP_LIMIT" and stop_price <= 0:
        st.warning("⚠ Stop Price must be greater than 0")
        st.stop()

    try:
        if order_type == "MARKET":
            order = place_market_order(symbol, side, quantity)

        elif order_type == "LIMIT":
            order = place_limit_order(symbol, side, quantity, price)

        else:
            order = place_stop_limit_order(
                symbol, side, quantity, stop_price, price
            )

        st.success("✅ Order placed successfully")
        st.json(order)

    except Exception as e:
        st.error(str(e))

        try:
            if order_type == "MARKET":
                order = place_market_order(symbol, side, quantity)

            elif order_type == "LIMIT":
                order = place_limit_order(symbol, side, quantity, price)

            else:
                order = place_stop_limit_order(
                    symbol, side, quantity, stop_price, price
                )

            st.success("Order placed successfully")
            st.json(order)

        except Exception as e:
            st.error(str(e))


# ================= ORDER HISTORY =================
with tab2:
    orders = load_orders()

    if not orders:
        st.info("📭 No orders found")
    else:
        for o in orders:
            st.json(o)

            if o.get("status") == "OPEN":
                if st.button(f"❌ Cancel Order ID {o['orderId']}"):
                    result = cancel_order(o["orderId"])
                    st.write(result)
                    st.experimental_rerun()
