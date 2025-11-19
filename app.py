from flask import Flask
app = Flask(__name__)
from config import Config
app.config.from_object(Config)

# Import your routes or logic from yamz.py if needed
# from yamz import some_blueprint_or_routes

