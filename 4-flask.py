from flask import Flask
import threading
import json, time
orderBook1 = __import__("1-orderBook")
price2 = __import__("2-price")

symbols = json.load(open("3-symbols.json"))

app = Flask(__name__)

def print(text):
    f = open(f"data/log.csv", "a")
    f.write(f"{text}\n")
    f.close()

def thread_function(name):
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

@app.route("/")
def index():
    f = open(f"data/log.csv", "r")
    result = "<br/>".join(f.readlines()) + """<a name="bottom"></a>"""
    f.close()
    return result


if __name__ == "__main__":
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
	)