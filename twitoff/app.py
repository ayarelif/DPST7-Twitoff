from flask import Flask
from .db_modul import DB, User
def create_app():
    '''Create and configure an instance of our Flask application'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Lambda School\\Unit3\\web_developer\\DPST7-Twitoff\\twitoff.sqlite3'
    DB.init_app(app)  # Connect Flask app to SQLAlchemy DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'
    

    @app.route('/<username>/<followers>')
    def add_user(username, followers):
        user=User(username=username, followers=followers)
        DB.session.add(user)
        DB.session.commit()

        return f'{username} has been added to the DB'

    return app
# export FLASK_APP=twitoff:APP ( in the terminal because of new module)
