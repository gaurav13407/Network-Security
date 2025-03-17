from networksecurity.components.Data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entitiy import DataIngestionConfig
from networksecurity.entity.config_entitiy import TraningpipelineConfig

if __name__=="__main__":
    try:
        
        traningpipleconfig=TraningpipelineConfig()
        dataingestionconfig=DataIngestionConfig(traningpipleconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initate The data ingesstion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)