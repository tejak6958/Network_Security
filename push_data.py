import numpy as np
import pandas as pd
import os
import json
import sys
from dotenv import load_dotenv
load_dotenv()
import certifi
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

MONGO_DB_URL = os.getenv("MONGO_API_KEY")


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def cv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def insert_data_mongo(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=certifi.where())

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]    
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "network_security"
    COLLECTION = "phishing_data"
    network_obj = NetworkDataExtract()
    records = network_obj.cv_to_json_converter(file_path = FILE_PATH)
    no_of_records = network_obj.insert_data_mongo(records,DATABASE,COLLECTION)
    print(no_of_records)
   
