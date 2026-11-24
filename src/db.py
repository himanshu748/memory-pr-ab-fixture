import os

from pymongo import MongoClient


def connect():
    return MongoClient(os.environ["DATABASE_URL"])["payments"]
