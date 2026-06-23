import logging
from typing import Tuple

from zenml import step
import pandas as pd
from sklearn.base import RegressorMixin
from typing_extensions import Annotated

from src.evaluation import Evaluation, MSE, R2, RMSE


@step
def evaluate_model(model: RegressorMixin,
    X_test: pd.DataFrame,
    y_test: pd.DataFrame,
) -> Tuple[
    Annotated[float, "r2_score"],
    Annotated[float, "rmse"],
]:

    """
    eval the model on ingested data
    """
    try:

        prediction = model.predict(X_test)
        mse_class = MSE()
        mse = mse_class.calculate(y_test, prediction)

        r2_class = R2()
        r2 = r2_class.calculate(y_test, prediction)

        rmse_class = RMSE()
        rmse = rmse_class.calculate_scores(y_test, prediction)
    except Exception as e:
        logging.error("Error occurred while evaluating model:{}".format(e))
        raise e
    