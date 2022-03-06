"""Contains variables used throughout the project."""
import os

PORT = int(os.environ.get("PORT", 5000))
TOKEN = os.environ[
    "TOKEN"]  # you need to create a config variable on heroku that is called TOKEN and has your bot api token as its value
