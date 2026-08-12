from pipelines.deployment_pipeline import deploy_pipeline, interence_pipeline
import click 

from pipelines.deployment_pipeline import deploy_pipeline, interence_pipeline
from pipelines.deployment_pipeline import continuous_deployment_pipeline
from rich import print
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri
from zenml.integrations.mlflow.model_deployers.mlflow_deployer import (
    MLFlowModelDeployer,
)
from zenml.integrations.mlflow.services import MLFlowDeploymentService

DEPLOY ="deploy"
PREDICT = "predict"
DEPLOY_AND_PREDICT = "deploy_and_predict"

@click.command()
@click.option(
    "--config",
    type=click.Choice([DEPLOY, PREDICT, DEPLOY_AND_PREDICT]),
    default=DEPLOY_AND_PREDICT,
    help="Optionally you can chooose to only deploy the deployment"
    "pipeline to train and deploy a model (`deploy`), or to "
    "only run a prediction against the deployed model "
    "(`predict`). By default both will run"
    "(`deploy_and_predict`).",

)

@click.option(
    "--min-accuracy",
    default=0.92,
    help="Minimum accuracy to deploy the model",
)

def run_deployment(config: str, min_accuracy: float):
    mlflow_model_deployer_component = MLFlowModelDeployer.get_active_model_deployer()
    deploy = config == DEPLOY or config == DEPLOY_AND_PREDICT
    predict = config == PREDICT or config == DEPLOY_AND_PREDICT

    if deploy:
        continuous_deployment_pipeline(
            min_accuracy,
            workers=3,
            timeout=60,)
    if predict:
        interence_pipeline()

    print(
        "You can run:\n"
        f"[italic green] mlflow ui --backend-store-uri {get_tracking_uri()}"
        "[/italic green]\n ...to inspect your experiment run within the MLFlow"
        "UI.\nYou can find your runs tracked within the "
        "`mlflow_example_pipleline` experiment. There you'll also be abelt to "
        "compare two or more runs.\n\n"
    )

    