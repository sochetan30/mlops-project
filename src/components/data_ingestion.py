import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import CustomException
import os 
import sys 
from sklearn.model_selection import train_test_split


from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    raw_data_path=os.path.join("artifact","raw.csv")
    train_data_path=os.path.join("artifact","train.csv")
    test_data_path=os.path.join("artifact","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started.")
        try:
            data=pd.read_csv("https://raw.githubusercontent.com/sochetan30/data_for_practice/main/gemstone.csv")
            logging.info("reading a dataframe.")
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True),
            data.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Saving raw data to to artifact folder")

            logging.info("Perform the train test split")
            train_data,test_data=train_test_split(data,test_size=0.25)

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("data ingestion part completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )



        except Exception as e:
            logging.info("Exception Occurred")
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()  
    obj.initiate_data_ingestion()      