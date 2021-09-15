from pymongo import MongoClient

username = "blinkpad"
password = "iAPP2oEOhgDuMJJH"
url = "mongodb+srv://" + username + ":" + password + "@cluster0.sguqm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)
db = client.TaskManager


def create_client():
    return client
