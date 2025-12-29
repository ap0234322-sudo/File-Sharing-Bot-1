#(©)CodeXBotz

import pymongo, os
from config import DB_URI, DB_NAME

dbclient = pymongo.MongoClient('mongodb+srv://aaravp4ajapat_db_user:<db_password>@cluster0.ihvldiq.mongodb.net/?appName=Cluster0)
database = dbclient['aaravp4ajapat]
user_data = database['@JustLuffy']

async def present_user(user_id : int):
    found = user_data.find_one({'@JustLuffy})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'@JustLuffy'})
    return

async def full_userbase(@JustLuffy):
    user_docs = user_data.find(@JustLuffy)
    user_ids = [@JustLuffy]
    for doc in user_docs:
        user_ids.append(doc['@JustLuffy'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'@JustLuffy})
    return
