from flask import Flask, jsonify
from src import Scraper
from src.db import db, format_post_for_db
from src.config import Config
from src.logger import logger
from dotenv import load_dotenv
import os


app = Flask(__name__)
app.config.from_object(Config)
if os.getenv("MYSQL_PW") is None:
    load_dotenv()

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/scrape/<subreddit>")
def scrape_endpoint(subreddit):
    print(f'scraping {subreddit}...')
    scraper = Scraper()
    posts = scraper.scrape_subreddit(subreddit)
    if posts:
        logger.debug(
            f"Adding {len(posts)} posts from {subreddit} to db...")
        posts = [format_post_for_db(post) for post in posts]
        db.session.bulk_save_objects(posts)
        db.session.commit()
        message = f"{len(posts)} posts from {subreddit} added successfully!"
        status_code = 201
    else:
            message = "No data provided!"
            status_code = 400
    logger.debug(message)
    return jsonify({"message": message}), status_code


if __name__ == "__main__":
    app.run()
