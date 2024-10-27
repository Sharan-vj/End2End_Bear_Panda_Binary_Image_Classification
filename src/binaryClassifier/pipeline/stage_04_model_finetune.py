# Import Dependencies
from binaryClassifier.logging import logger
from binaryClassifier.components.model_finetune import ModelFinetuner
from binaryClassifier.config.configuration import ConfigManager

# Stage Name
STAGE_NAME = ""

# Model Finetuning Pipeline
class ModelFinetunePipeline:
    def __init__(self):
        pass

    def initiate_model_finetuning(self):
        config = ConfigManager()
        model_finetune_config = config.get_model_finetune_config()
        model_finetuner = ModelFinetuner(config=model_finetune_config)
        model_finetuner.finetune_model()


if __name__ == '__main__':
    try:
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
        obj = ModelFinetunePipeline()
        obj.initiate_model_finetuning()
        logger.info(msg=f">>>>> STAGE {STAGE_NAME} FINISHED <<<<<")
    except Exception as e:
        logger.exception(msg=e)
        raise e