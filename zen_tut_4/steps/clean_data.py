import logging

import pandas as pd
from zenml import step


from src.data_cleaning import DataCleaning, DataDivideStrategy, DataPreProcessStrategy
from typing_extensions import Annotated
from typing import Tuple

@step
def clean_df(df: pd.DataFrame) -> Tuple[ 
    Annotated[pd.DataFrame, "x_train"], 
    Annotated[pd.DataFrame, "x_test"], 
    Annotated[pd.Series, "y_train"], 
    Annotated[pd.Series, "y_test"],
]:
    """
    clean the data and divide it into train and test

    Args:
        df raw data
    Returns:
        x_train: train data
        x_test: test data
        y_train: train labels
        y_test: test labels
    """
    try:
        process_strategy = DataPreProcessStrategy()
        data_cleaning = DataCleaning(df, process_strategy)
        processed_data = data_cleaning.handle_data()

        divide_strategy = DataDivideStrategy()
        data_cleaning = DataCleaning(processed_data, divide_strategy)
        X_train, X_test, y_train, y_test = data_cleaning.handle_data()
        logging.info("Data cleaning and division completed successfully.")
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logging.error("Error in cleaning data: {}".format(e)) 
        raise e