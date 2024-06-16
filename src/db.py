from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'second_seide'
    id = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    selftext = db.Column(db.Text, nullable=False)
    created_utc_timestamp = db.Column(db.Float, nullable=False)
    created_date = db.Column(db.String(255), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    num_comments = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    subreddit = db.Column(db.String(255), nullable=False)


def format_post_for_db(post):
    new_post = Post(
        id=post.get('id'),
        title=post.get('title'),
        selftext=post.get('selftext'),
        created_utc_timestamp=post.get('created_utc_timestamp'),
        created_date=post.get('created_date'),
        score=post.get('score'),
        num_comments=post.get('num_comments'),
        url=post.get('url'),
        subreddit=post.get('subreddit')
    )
    return new_post
