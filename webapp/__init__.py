from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") #environment variable for secret key configuration

    from .moods import moods

    app.register_blueprint(moods, url_prefix='/')

    return app

    
    