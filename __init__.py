from unicodedata import name
from flask import Flask

# initializing application
app = Flask ( __name__)

from watchlist import view