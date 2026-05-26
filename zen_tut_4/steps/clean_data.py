import logging

import pandas as pd
from zenml import step
from src.data_cleaning import DataCleaning, DataDivideStrategy, DataPreProcessStrategy

@step
def clean_df(df: pd.DataFrame) -> None:
    try:
        process_str 