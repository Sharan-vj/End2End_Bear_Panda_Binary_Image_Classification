# Import Dependencies
from binaryClassifier.logging import logger
from binaryClassifier.components.data_validation import DataValidation
from binaryClassifier.config.configuration import ConfigManager

# Stage Name
STAGE_NAME = "DATA VALIDATION"

# Data Validation Pipeline
class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_data()


if __name__ == '__main__':
    try:
        logger.info(msg=f"STAGE {STAGE_NAME} STARTED")
        obj = DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(msg=f"STAGE {STAGE_NAME} COMPLETED")
    except Exception as e:
        logger.exception(msg=e)
        raise e