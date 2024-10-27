# Import Dependencies
from binaryClassifier.constants import *
from binaryClassifier.entity.config_entity import *
from binaryClassifier.utils.common import create_directory, yaml_reader

# Config Manager Class
class ConfigManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        
        self.config = yaml_reader(filepath=config_filepath, log=True)
        self.params = yaml_reader(filepath=params_filepath, log=True)
        create_directory(directory_path=[self.config.artifacts_root], log=True)


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory(directory_path=[config.root_dir], log=True)

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            dataset_url=config.dataset_url,
            dataset_raw=config.dataset_raw
        )
        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directory(directory_path=[config.root_dir], log=True)

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            dataset_path=config.dataset_path,
            status_file=config.status_file
        )
        return data_validation_config


    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.base_model
        params = self.params.VGG19
        create_directory(directory_path=[config.root_dir], log=True)

        base_model_config = BaseModelConfig(
            root_dir=config.root_dir,
            base_model=config.base_model,
            model_save=config.model_save,
            weights=params.WEIGHTS,
            include_top=params.INCLUDE_TOP,
            image_size=params.IMAGE_SIZE
        )
        return base_model_config

    def get_model_finetune_config(self) -> ModelFinetuneConfig:
        config = self.config.model_finetune
        params = self.params.VGG19
        create_directory(directory_path=[config.root_dir], log=True)

        model_finetune_config = ModelFinetuneConfig(
            root_dir=config.root_dir,
            base_model=config.base_model,
            model_weights=config.model_weights,
            train_data=config.train_data,
            target_size=params.TARGET_SIZE,
            learning_rate=params.LEARNING_RATE,
            epochs=params.EPOCHS,
            batch_size=params.BATCH_SIZE
        )
        return model_finetune_config