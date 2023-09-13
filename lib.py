from pymongo import MongoClient
import os
import re


def initcol():
    url = os.getenv("MONGO_SERVER")
    myclient = MongoClient(url)
    dbname = "persons"
    mydb = myclient[dbname]
    return mydb["persons"]


def isvalid(string):
    return re.match(r"^([A-Za-z]+\s*)+$", string)
