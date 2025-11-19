import sys
import os
sys.path.append(os.path.dirname(__file__))  # ensures top-level folder is in path

from config import Config
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)

