"""Code for our app."""

from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

# make our app factory


def create_app():
    """Create App using function."""
    app = Flask(__name__)

    # stop tracking modifications on SQLAlchemy config

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    # have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset', users=[])

    return app
