import logging

from zenml import step
import pandas as pd
from src.evaluation import Evaluation, MSE, R2, RMSE


@step
def evaluate_model(df: pd.DataFrame) -> None:
    pass