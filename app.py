from flask import Flask, jsonify
from src import scrape_subreddit
from src.config import SUBREDDITS
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()


@app.route("/scrape/<subreddit>")
def scrape_endpoint(subreddit):
    posts = scrape_subreddit(subreddit)
    return jsonify(posts)


if __name__ == "__main__":
    app.run()
