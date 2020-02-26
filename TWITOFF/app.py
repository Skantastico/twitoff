"""Code for our app."""

from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

from .twitter import add_or_update_user

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

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        try:
            if request.method == 'POST':
                add_or_update_user(name)
                message = "User {} successfully added".format(name)
            tweets = User.query.filter(User.name == name).one().tweets
        except Exception as e:
            pass

    return app
