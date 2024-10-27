# Import Dependencies
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.callbacks import EarlyStopping # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore

from binaryClassifier.logging import logger
from binaryClassifier.entity.config_entity import ModelFinetuneConfig

# Model Finetune Components
class ModelFinetuner:
    def __init__(self, config: ModelFinetuneConfig):
        self.config = config

    
    def finetune_model(self):
        image_datagen = ImageDataGenerator(
            rotation_range=20,
            width_shift_range=0.10,
            height_shift_range=0.10,
            rescale=1.255,
            shear_range=0.1,
            zoom_range=0.1,
            horizontal_flip=True,
            fill_mode='nearest'
        )

        train_datagen = image_datagen.flow_from_directory(
            directory=self.config.train_data,
            target_size=self.config.target_size,
            batch_size=self.config.batch_size,
            class_mode='binary',
            color_mode='rgb'
        )

        model = load_model(self.config.base_model)
        optim = Adam(learning_rate=self.config.learning_rate)
        model.compile(optimizer=optim, loss='binary_crossentropy', metrics=['accuracy'])
        early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
        
        history = model.fit(x=train_datagen,
                            epochs=self.config.epochs)
        
        model.save_weights(self.config.model_weights)
        logger.info(msg=f"Model Weights saved to : {self.config.model_weights}")