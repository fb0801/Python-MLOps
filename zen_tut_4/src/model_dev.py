import logging
from abc import ABC, abstractmethod 
from sklearn.linear_model import LinearRegression

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

class LinearRegressionModel(Model):

    """
    linear regression model
    """
    def train(self, x_train, y_train, **kwargs):
        """
        trains the model
        Args:
            x_train: training data
            y_train: training labels
        Returns:
            None
        """
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(x_train, y_train)
            logging.info("Model training completed")
            return reg
        except Exception as e:
            logging.error("Error in training the model: {}".format(e))
            raise e 