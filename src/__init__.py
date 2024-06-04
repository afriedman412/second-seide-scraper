import praw
from time import sleep
import os


def create_reddit():
    reddit = praw.Reddit(
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        user_agent=os.environ["USER_AGENT"]
    )
    return reddit


def scrape_subreddit(subreddit, cooldown=5):
    reddit = create_reddit()
    results = []

    s = reddit.subreddit(subreddit)
    print(f'scraping {subreddit}...')
    for n, submission in enumerate(s.new(limit=10)):
        post_data = {
            'id': submission.id,
            'title': submission.title,
            'selftext': submission.selftext,
            'created_utc': submission.created_utc,
            'score': submission.score,
            'num_comments': submission.num_comments,
            'url': submission.url
        }
        results.append(post_data)
        if not n % 5:
            sleep(cooldown)
    return results