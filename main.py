from flask import Flask, render_template, redirect, url_for, request
import string
import random

app = Flask(__name__)

shortened_urls = {}

def generate_shortened_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form["original_url"]
        shortened_url = generate_shortened_url()
        
        while shortened_url in shortened_urls:
            shortened_url = generate_shortened_url()
        
        shortened_urls[shortened_url] = original_url
        return render_template("index.html", shortened_url=shortened_url)
    
    return render_template("index.html")

@app.route("/<shortened_url>")
def redirect_url(shortened_url):
    original_url = shortened_urls.get(shortened_url)

    if original_url:
        return redirect(original_url)
    else:
        return "Shortened URL not found", 404
    

if __name__ == "__main__":
    app.run(debug=True)
