import  logging
import pandas as pd
from zenml import step


from src.model_dev import LinearRegressionModel
from sklearn.base import RegressorMixin

@step
def train_model(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.DataFrame,
    y_test: pd.DataFrame,

) -> RegressorMixin:
    """
    trains the model on the ingested data
    Args:
        df: ingested data
    """
    model = None