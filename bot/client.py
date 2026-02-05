from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_binance_client():
    api_key = os.getenv("iRQsTjLMpL3OA6NslyVhRqkgMG09RwLOTC45rnZtdoXHx6NSWsjyWfCTcB4JLWkt")
    api_secret = os.getenv("XOyBHeYSRdt5mf7H4LxSGlopr1f8QICb1ZAGdfUJQxOfdsilFJBcSGFxHhcYitbT")

    if not api_key or not api_secret:
        raise ValueError("API keys not found in .env")

    client = Client(api_key, api_secret)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    return client
