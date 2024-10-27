# Import Dependencies
import os
import gdown
import zipfile
from binaryClassifier.logging import logger
from binaryClassifier.entity.config_entity import DataIngestionConfig


# Data Ingestion Component
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_dataset(self):
        try:
            dataset_url = self.config.dataset_url
            dataset_raw = self.config.dataset_raw
            os.makedirs(self.config.root_dir, exist_ok=True)

            logger.info(msg=f"Downloading dataset from {dataset_url} url")
            drive_prefix = "https://drive.google.com/uc?/export=download&id="
            file_id = dataset_url.split("/")[-2]
            gdown.download(url=drive_prefix+file_id, output=dataset_raw)
            logger.info(msg=f"Dataset stored at {dataset_raw}")

        except Exception as e:
            logger.exception(msg=e)
            raise e
        
    def extract_dataset(self):
        logger.info(msg=f"Extracting dataset: {self.config.dataset_raw}")
        unzip_dir = self.config.root_dir
        with zipfile.ZipFile(file=self.config.dataset_raw, mode='r') as zip:
            zip.extractall(path=unzip_dir)
        logger.info(msg=f"Dataset Extracted at {self.config.root_dir}")
    