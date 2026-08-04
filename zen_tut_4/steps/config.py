from zenml.steps import BaseParameters

class ModelNameConfig(BaseParameters):
    """model config"""
    model_name: str = "LinearRegression"
    