import os
import sys
import numpy as np
import pandas as pd

'''
define common constant variable for traning pipeline
'''
TARGET_COLUMN="phishing"
PIPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="Aritifacts"
FILE_NAME:str="dataset.csv"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

SCHMEA_FILE_PATH=os.path.join("data_schema","schema.yaml")

'''
Data Ingestion related constant start with Data_Ingestion VAR Name
'''

DATA_INGESTION_COLEECTION_NAME:str="NetworkData"
DATA_INGESTION_DATABASE_NAME:str="GAURAV"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPILT_RATION:float=0.2

"""
Data Validation related constant start with DATA_VALIDATION VAR NAME 
"""
DATA_VALIDATION_DIR_NAME:str="data_validation"
DATA_VALIDATION_VALID_DIR:str="validated"
DATA_VALIDATION_INVALID_DIR:str="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report.yaml"