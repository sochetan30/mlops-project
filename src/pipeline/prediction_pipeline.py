import os
import sys
import pandas as pd
from src.exception.exception import CustomException
from src.logger.logging import logging
from src.utils.utils import load_object

class PredictPipeline:

    def __init__(self):
        print("initializing the object")