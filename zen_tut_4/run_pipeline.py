from pipelines.training_pipeline import train_pipeline
#from zenml.clinet import Client

if __name__ == "__main__":
    train_pipeline(
        data_path="data/olist_customers_dataset.csv"
    )
