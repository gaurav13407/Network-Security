from networksecurity.components.Data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entitiy import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entitiy import TraningpipelineConfig

if __name__=="__main__":
    try:
        
        traningpipleconfig=TraningpipelineConfig()
        dataingestionconfig=DataIngestionConfig(traningpipleconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initate The data ingesstion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion is completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(traningpipleconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("initate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation is completed")
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(traningpipleconfig)
        logging.info("Data Transfromation Started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Datat Transformation Completed")
        
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)