from pipelines.deployment_pipeline import deploy_pipeline, interence_pipeline
import click 


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

def run_deployment(confi: str, min_accuracy: float):
    if deploy:
        deploy_pipeline(min_accuracy)
    if predict:
        interence_pipeline()