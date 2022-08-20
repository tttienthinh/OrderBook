import json, time
orderBook1 = __import__("1-orderBook")
price2 = __import__("2-price")

symbols = json.load(open("3-symbols.json"))

"""
création csv

for symbol in symbols:
    f = open(f"data/{symbol}.csv", "w")
    f.write("time, price, \
        bids_avg, bids_Q1, bids_Q2, bids_Q3, bids_mode, bids_sum, \
        asks_avg, asks_Q1, asks_Q2, asks_Q3, asks_mode, asks_sum \n")
    f.close()
"""

while True:
    remaining_sec = 60 - (time.time()%60)
    time.sleep(remaining_sec)
    print(f"--- {time.asctime()}")
    for symbol in symbols:
        codeBook,  book  = orderBook1.toLineTextAnalyse(symbol=symbol)
        codePrice, price = price2.getPrice(symbol)
        if codeBook and codePrice:
            f = open(f"data/{symbol}.csv", "a")
            f.write(f"{time.time()}, {price}, {book}\n")
            f.close()
        else:
            print(f"{symbol} : {codeBook} {codePrice}")
    print(f"    {time.asctime()} ---")

