import requests, json

LINK = "https://api.binance.com/api/v3/ticker/price"

def getOrderBook(symbol="BTCUSDT"):
    payload = {
        "symbol":symbol
    }
    r = requests.get(
        LINK,
        params=payload
    )
    if r.status_code == 200:
        return True, r.json()
    else:
        print("Erreur getOrderBook")
        return False, {}

def getPrice(symbol="BTCUSDT"):
    code, data = getOrderBook(symbol)
    if code:
        return True, data["price"]
    else:
        return False, ""

if __name__ == "__main__":
    getPrice()
