import logging
from abc import ABC, abstractmethod

from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class Evaluation(ABC):
    """
    Abstract class for model evaluation"""
    
    @abstractmethod
    def calculate_scores(self, y_true: np.ndarray,y_pred: np.ndarray):
        """
        Abstract method to calculate evaluation scores
        Args:
            y_true: true labels
            y_pred: predicted labels
        Returns:
            None
        """
        pass

class MSE(Evaluation):
    """
    evaluation strategy for calculating mean squared error
    """
    def calculate_scores(self, y_true: np.ndarray,y_pred: np.ndarray):
        try:
            logging.info("Calculating mean squared error")
            mse = mean_squared_error(y_true, y_pred)
            logging.info("MSE: {}".format(mse))
            return mse
        except Exception as e:
            logging.error("Error in calculating MSE: {}".format(e))
            raise e
        
class R2(Evaluation):
    """
    evaluation strategy for calculating r2 score
    """
    def calculate_scores(self, y_true: np.ndarray,y_pred: np.ndarray):
        try:
            logging.info("Calculating r2 score")
            r2 = r2_score(y_true, y_pred)
            logging.info("R2: {}".format(r2))
            return r2
        except Exception as e:
            logging.error("Error in calculating R2: {}".format(e))
            raise e
        
class RMSE(Evaluation):
    """
    evaluation strategy for calculating root mean squared error
    """
    def calculate_scores(self, y_true: np.ndarray,y_pred: np.ndarray):
        try:
            logging.info("Calculating root mean squared error")
            rmse = mean_squared_error(y_true, y_pred, squared=False)
            logging.info("RMSE: {}".format(rmse))
            return rmse
        except Exception as e:
            logging.error("Error in calculating RMSE: {}".format(e))
            raise e