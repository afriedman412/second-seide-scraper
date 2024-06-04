from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'second_seide'  # The name of the table
    id = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    selftext = db.Column(db.Text, nullable=False)
    created_utc = db.Column(db.Float, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    num_comments = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(255), nullable=False)


def add_posts(data):
    if data:
        posts = []
        for item in data:
            new_post = Post(
                id=item.get('id'),
                title=item.get('title'),
                selftext=item.get('selftext'),
                created_utc=item.get('created_utc'),
                score=item.get('score'),
                num_comments=item.get('num_comments'),
                url=item.get('url')
            )
            posts.append(new_post)
        db.session.bulk_save_objects(posts)
        db.session.commit()
        return {"message": "Posts added successfully!"}, 201
    else:
        return {"message": "No data provided!"}, 400
