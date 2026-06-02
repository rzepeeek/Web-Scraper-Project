from flask import Flask, request
from scraper.worker import run_parallel
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
db = client["scraper_db"]

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.json
    urls = data.get("urls", [])

    batches = [urls[i:i+5] for i in range(0, len(urls), 5)]
    results = run_parallel(batches)

    print(results)  

    collection = db["data"]

    for batch in results:
        collection.insert_many(batch)

    return {"status": "done"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)