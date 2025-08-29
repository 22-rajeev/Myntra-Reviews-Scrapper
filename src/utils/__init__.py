from src.cloud_io import MongoIO
from src.constants import MONGO_DATABASE_NAME
from src.exception import CustomException
import os , sys

def fetch_product_names_from_cloud():
    try:
        mongo = MongoIO()
        collection_names = mongo.mongo_ins.mongo_operation__connect_database.list_collect_names()
        return [ collection_names.replace('_' ,' ') for collection_name in collection_names]
    except Exception as e:
        raise CustomException(e , sys)