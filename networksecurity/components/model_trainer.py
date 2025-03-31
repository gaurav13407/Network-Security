import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from networksecurity.entity.config_entitiy import ModleTrainerConfig

from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.utils.main_utils.utils import save_object,load_object
from networksecurity.utils.main_utils.utils import load_numpy_array_data,evaluate_models
from networksecurity.utils.ml_utils.metric.classifiaction_metric import get_classification_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import(
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier
)

class ModelTrainer:
    def __init__(self,model_trainer_config:ModleTrainerConfig,data_transformation_artifact:DataTransformationArtifact):
        
        try:
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact=data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
    def train_model(self,x_train,y_train,x_test,y_test):
        models={
            "Random Forest":RandomForestClassifier(verbose=1),
            "Decision tree":DecisionTreeClassifier(),
            "Gradient Bossting":GradientBoostingClassifier(verbose=1),
            "Logistic Regessor":LogisticRegression(verbose=1),
            "Ada Bosst":AdaBoostClassifier(),
        }
        
    params={
        "Decision Tree":{
            'criterion':['gini','entropy','log_loss'],
            'splitter':["best", "random"],
            'max_features':['sqrt','log2']
        },
        "Random Forest":{
            'criterion':['gini','entropy','log_loss'],
            'max_features':['sqrt','log2','None'],
            'n_estimators':[8,16,32,64,128,256]
        },
        "Gradient Bossting":{
            'loss':['log_loss','exponential'],
            'learning_rate':[0.6,0.7,0.75,0.8,0.85,0.9],
            'criterion':['squared_error','friedman_mse'],
            'max_features':['sqrt','log2','None'],
            'n_estimators':[8,16,32,64,128,256]
        },
        "logisting Regressor":{},
        "AdaBoost":{
            'learning_rate':[0.1,0.01,0.5,0.001],
            'n_estimators':[8,16,32,64,128,256]
        }
    }
    
    # Evaluate models
    model_report = evaluate_models(
            X_train=x_train, X_test=x_test, y_train=y_train, y_test=y_test,
            models=models, params=params
        )
        
    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            train_file_path=self.data_transformation_artifact.transformed_train_file_path
            test_file_path=self.data_transformation_artifact.transformed_test_file_path
            
            # loading trainig array and testing array
            train_arr=load_numpy_array_data(train_file_path)
            test_arr=load_numpy_array_data(test_file_path)
            
            x_train,x_test,y_train,y_test=(
                train_arr[:,:-1],
                train_arr[:,:-1],
                test_arr[:,:-1],
                test_arr[:,:-1]
            )
            
            model=self.train_model(x_train,y_train,x_test,y_test)
        except Exception as e:
            raise NetworkSecurityException(e,sys)