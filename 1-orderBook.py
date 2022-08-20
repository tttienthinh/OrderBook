import requests, json
import pandas as pd
import numpy as np

LINK = "https://api.binance.com/api/v3/depth"

def getOrderBook(limit=5_000, symbol="BTCUSDT"):
    payload = {
        "limit": limit,
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

"""
Renvoie les données brutes (trop lourdes env. 200ko)
"""
def toLineText(limit=5_000, symbol="BTCUSDT"):
    code, data = getOrderBook(limit, symbol)
    if code:
        textBids = ", ".join([", ".join(order) for order in data["bids"]])
        textAsks = ", ".join([", ".join(order) for order in data["asks"]])
        return True, f"{textBids}, {textAsks}"
    else:
        return False, ""

""""
Moyen d'analyser les données
"""
def analyse(data):
    df = pd.DataFrame(data, columns=["data", "weight"], dtype=float)

    somme = df["weight"].sum()
    moyenne = (df["data"]*df["weight"]).sum() / somme
    mode = df["data"][df["weight"].idxmax()]
    df["cumsum"] = df["weight"].cumsum()
    Q1 = df["data"][df["cumsum"] >= (somme*0.25)].iloc[0]
    Q2 = df["data"][df["cumsum"] >= (somme*0.50)].iloc[0]
    Q3 = df["data"][df["cumsum"] >= (somme*0.75)].iloc[0]

    return [str(val) for val in [moyenne, Q1, Q2, Q3, mode, somme]]


def toLineTextAnalyse(limit=5_000, symbol="BTCUSDT"):
    code, data = getOrderBook(limit, symbol)
    if code:
        textBids = ", ".join(analyse(data["bids"]))
        textAsks = ", ".join(analyse(data["asks"]))
        return True, f"{textBids}, {textAsks}"
    else:
        return False, ""
    

if __name__ == "__main__":
    data = getOrderBook(500)
    json.dump(data, open("file.json", "w"))