from flask_sqlalchemy import SQLAlchemy
"""Making the models for my app"""

DB = SQLAlchemy()


class User(DB.Model):
    """Twitter users that we analyze."""

    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)


class Tweet(DB.Model):
    """Tweets we pull."""

    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey()'user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
