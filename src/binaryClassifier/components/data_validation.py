# Import Dependencies
import os
from binaryClassifier.logging import logger
from binaryClassifier.entity.config_entity import DataValidationConfig

# Data Validation Component
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    
    def validate_data(self):
        try:
            validation_status = None
            dataset_path = self.config.dataset_path
            train_dir = os.path.join(dataset_path, 'train')
            test_dir = os.path.join(dataset_path, 'test')

            if os.path.isdir(train_dir) and os.path.isdir(test_dir):
                validation_status = True
                with open(self.config.status_file, 'w') as f:
                    f.write(f"validation status: {validation_status}")
                    logger.info(msg=f"validation status: {validation_status}")
            else:
                validation_status = False
                with open(self.config.status_file, 'w') as f:
                    f.write(f"validation status: {validation_status}")
                    logger.info(msg=f"validation status: {validation_status}")
        except Exception as e:
            logger.exception(msg=e)
            raise e
