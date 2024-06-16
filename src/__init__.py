from datetime import datetime as dt
import os
from time import sleep

import praw

from .config import DT_FORMAT
from .logger import logger


class Scraper:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.environ["CLIENT_ID"],
            client_secret=os.environ["CLIENT_SECRET"],
            user_agent=os.environ["USER_AGENT"]
        )
        return

    def scrape_subreddit(self, subreddit: str, cooldown: int = 5, post_limit: int = 10):
        logger.debug(f"Scraping {subreddit}...")
        posts = []
        s = self.reddit.subreddit(subreddit)
        for n, post in enumerate(s.new(limit=post_limit)):
            post_data = {
                'id': post.id,
                'title': post.title,
                'selftext': post.selftext,
                'created_utc_timestamp': post.created_utc,
                'score': post.score,
                'num_comments': post.num_comments,
                'url': post.url
            }

            post_data['created_date'] = dt.strftime(
                dt.fromtimestamp(post_data['created_utc_timestamp']),
                DT_FORMAT
            )
            post_data['subreddit'] = subreddit
            posts.append(post_data)
            if not n % 5:
                sleep(cooldown)
        return posts

