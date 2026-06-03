import logging
from abc import ABC, abstractmethod 

class Model(ABC):

    @abstractmethod
    def train(self, x_train, y_train):
        """
        Trains the model 
        args:
        x_train: training data
        y_train: training labels
        returns:
        None
        """
        pass