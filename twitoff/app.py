from flask import Flask

def create_app():
    """ Create and configure an instance of our flask application"""
    app=Flask(__name__)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff:'
        
    return app