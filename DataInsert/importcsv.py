import csv
from Client.connectMongo import connectDB

with open("information.csv", 'r', encoding = 'utf-8') as f:
    row = csv.DictReader(f)
    for each in row:
        dicts = dict(each)
        print(dicts)
        collection = connectDB(Collection = "studentInformation")
        collection.insert_one(dicts)