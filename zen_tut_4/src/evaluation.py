import logging
from abc import ABC, abstractmethod
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