import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import CustomException
import os 
import sys 

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from skleaar.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataTransformationConfig:
    pass

class DataTransformation:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)