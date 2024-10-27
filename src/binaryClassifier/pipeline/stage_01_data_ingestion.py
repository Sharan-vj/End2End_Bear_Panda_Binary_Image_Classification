# Import Dependencies
from binaryClassifier.logging import logger
from binaryClassifier.components.data_ingestion import DataIngestion
from binaryClassifier.config.configuration import ConfigManager

# Stage Name
STAGE_NAME = "DATA INGESTION"


# Data Ingestion Pipeline
class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_dataset()
        data_ingestion.extract_dataset()

if __name__ == '__main__':
    try:
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} COMPLETED <<<<<")
    except Exception as e:
        logger.exception(msg=e)
        raise e