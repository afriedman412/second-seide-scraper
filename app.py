from flask import Flask, jsonify
from src import scrape_subreddit
from src.db import db, add_posts
from src.config import Config
from dotenv import load_dotenv
import os


app = Flask(__name__)
app.config.from_object(Config)
if os.getenv("MYSQL_PW") is None:
    load_dotenv()

db.init_app(app)


@app.route("/scrape/<subreddit>")
def scrape_endpoint(subreddit):
    print(f'scraping {subreddit}...')
    posts = scrape_subreddit(subreddit)
    print("updating table...")
    response, status_code = add_posts(posts)
    return jsonify(response), status_code


if __name__ == "__main__":
    app.run()
