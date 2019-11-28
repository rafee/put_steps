import pymongo
import sys
import datetime
from bson.objectid import ObjectId


def put_steps(event, context):
    # Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
    username = "chamseddine"
    password = "123456chams"
    db_cluster = "cloud-concordia"
    client = pymongo.MongoClient(
        f'mongodb://{username}:{password}@{db_cluster}.cluster-cxfjdmvmj3tw.us-east-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0')

    # Specify the database to be used
    db = client.test

    # Specify the collection to be used
    col = db.datas

    # Insert a single document
    uid = event['id']
    #date = datetime.datetime.today().date()
    #date=datetime.datetime.combine(date, datetime.time.min)
    date=event['date']
    date=datetime.datetime.fromtimestamp(date/1000.0)
    date=datetime.datetime.combine(date, datetime.time.min)
    steps = event['steps']
    sleepingHours=event['sleepingHours']
    col.update(
        {
            "correspond": ObjectId(uid),
            "date":date
        },
        {
            "$set": 
                {
                    "steps": steps,
                    "sleepingHours":sleepingHours,
                    "__v":0,
                },
                
        },
        upsert=True
    )
    # col.insert_one({'hello': 'Amazon DocumentDB'})

    # Close the connection
    client.close()
    return event