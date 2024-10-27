# Import Dependencies
from binaryClassifier.logging import logger
from binaryClassifier.components.base_model import BaseModel
from binaryClassifier.config.configuration import ConfigManager

# Stage name
STAGE_NAME = " "


# Base Model Pipeline
class BaseModelPipeline:
    def __init__(self):
        pass
    
    def initiate_build_base_model(self):
        config = ConfigManager()
        base_model_config = config.get_base_model_config()
        base_model = BaseModel(config=base_model_config)
        base_model.build_base_model()


if __name__ == "__main__":
    try:
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
        obj = BaseModelPipeline()
        obj.initiate_build_base_model()
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} FINISHED <<<<<")
    except Exception as e:
        logger.exception(msg=e)
        raise e