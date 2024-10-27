# Import Dependencies
from binaryClassifier.logging import logger
from binaryClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from binaryClassifier.pipeline.stage_02_data_validation import DataValidationPipeline
from binaryClassifier.pipeline.stage_03_base_model import BaseModelPipeline
from binaryClassifier.pipeline.stage_04_model_finetune import ModelFinetunePipeline

# Data Ingestion Pipeline
STAGE_NAME = "DATA INGESTION"
try:
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} COMPLETED <<<<<")
except Exception as e:
    logger.exception(msg=e)
    raise e

# Data Validation Pipeline
STAGE_NAME = "DATA VALIDATION"
try:
    logger.info(msg=f"STAGE {STAGE_NAME} STARTED")
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(msg=f"STAGE {STAGE_NAME} COMPLETED")
except Exception as e:
    logger.exception(msg=e)
    raise e

# Base Model Pipeline
STAGE_NAME = "BASE MODEL PIPELINE"
try:
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
    obj = BaseModelPipeline()
    obj.initiate_build_base_model()
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} FINISHED <<<<<")
except Exception as e:
    logger.exception(msg=e)
    raise e

# Model Finetune Pipeline
try:
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
    obj = ModelFinetunePipeline()
    obj.initiate_model_finetuning()
    logger.info(msg=f">>>>> STAGE {STAGE_NAME} FINISHED <<<<<")
except Exception as e:
    logger.exception(msg=e)
    raise e