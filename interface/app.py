from flask import Flask, request, render_template
import requests

app = Flask(__name__)

ENGINE_URL = "http://engine:5001/scrape"

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        urls = request.form["urls"].split(",")
        urls = [u.strip() for u in urls if u.strip()]

        try:
            requests.post(ENGINE_URL, json={"urls": urls})
            message = "Scrapowanie rozpoczęte!"
        except:
            message = "Błąd połączenia z silnikiem."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)