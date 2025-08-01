from utils.common_functions import read_yaml
from config.paths_config import *
from src.data_processing import DataProcessor
from src.model_training import ModelTraining

if __name__=="__main__":
    data_processor = DataProcessor(ANIMELIST_CSV,PROCESSED_DIR)
    data_processor.run()

    model_trainer = ModelTraining(PROCESSED_DIR)
    model_trainer.train_model()

'''

We will remove this data ingestion.

We will remove this data ingestion from our training pipeline.

Why?

Why we are removing.

Okay, so there is a reason why we are doing this.

Basically data ingestion is used to, uh, extract your data from the GCP bucket.

Right.

Now what data ingestion is doing.

GCP bucket to your PC.

Okay.

But in the next step that is our data versioning.

What are we going to do.

All the things in our artifacts folder.

All the things in our artifacts folder will be pushed to another GCP bucket.

Another GCP bucket okay.

And whenever we need those artifacts we will just do the pull from DVC.

We will extract that data from DVC.

So inside artifact we have the raw folder also.

So why we need data ingestion because we are pulling that data from DVC.

Okay.

So that's why we don't need the data ingestion part.


'''