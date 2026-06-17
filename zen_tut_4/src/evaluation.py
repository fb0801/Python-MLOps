import logging
from abc import ABC, abstractmethod

from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class Evaluation(ABC):
    """
    Abstract class for model evaluation"""
    
    @abstractmethod
    def calculate_scores(self, y_true: np.ndarray,y_pred: np.darray):
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
    def calculate_scores(self, y_true: np.ndarray,y_pred: np.darray):
        try:
            logging.info("Calculating mean squared error")
            mse = mean_squared_error(y_true, y_pred)
            logging.info("MSE: {}".format(mse))
        except Exception as e:
            logging.error("Error in calculating MSE: {}".format(e))
            raise e
        