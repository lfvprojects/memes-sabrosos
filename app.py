# !/bin/python

from flask import Flask, render_template
import requests
import json
import os

server = os.environ.get("server")
app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_lrg = response["preview"] [-2]
    subreddit = response["subreddit"]
    return meme_lrg, subreddit

@app.route("/")
def index():
    meme_img, subreddit = get_meme()
    return render_template("index.html", meme_img=meme_img, subreddit=subreddit, server=server)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
