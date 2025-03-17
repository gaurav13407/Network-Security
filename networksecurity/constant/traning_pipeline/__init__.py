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

'''
Data Ingestion related constant start with Data_Ingestion VAR Name
'''

DATA_INGESTION_COLEECTION_NAME:str="NetworkData"
DATA_INGESTION_DATABASE_NAME:str="GAURAV"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPILT_RATION:float=0.2