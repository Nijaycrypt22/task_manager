from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# connect to mongo atlas cluster
mongo_client = MongoClient("mongodb+srv://task_manager:task_manager@growcohort6.tsuz7zi.mongodb.net/")

# access the database
task_manager_db= mongo_client["task_manager_db"]

# pick a database to operate on
tasks= task_manager_db["tasks"]