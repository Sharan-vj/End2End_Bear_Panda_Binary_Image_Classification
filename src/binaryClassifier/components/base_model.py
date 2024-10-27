# Import Dependencies
import tensorflow as tf
from tensorflow.keras.models import Model, save_model # type: ignore
from tensorflow.keras.applications import VGG19 # type: ignore
from tensorflow.keras.layers import Dense, Dropout, Flatten # type: ignore

from binaryClassifier.logging import logger
from binaryClassifier.entity.config_entity import BaseModelConfig

# Base Model Component
class BaseModel:
    def __init__(self, config: BaseModelConfig):
        self.config = config

    def build_base_model(self):
        # load VGG19 without top layers
        vgg19 = VGG19(weights=self.config.weights,
                           include_top=self.config.include_top,
                           input_shape=self.config.image_size)
        
        # add custom top layers
        x = Flatten()(vgg19.output)
        x = Dense(units=128, activation='relu')(x)
        x = Dropout(rate=0.5)(x)
        output = Dense(units=1, activation='sigmoid')(x)

        # create the final model
        model = Model(inputs=vgg19.input, outputs=output)

        # freeze the layers of VGG19 to avoid retraining them
        for layer in vgg19.layers:
            layer.trainable = False

        # save base model
        save_model(model, self.config.base_model)
        save_model(model, self.config.model_save)
        logger.info(f'Base model saved to {self.config.base_model}')

