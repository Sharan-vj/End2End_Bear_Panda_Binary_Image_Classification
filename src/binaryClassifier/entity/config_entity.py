# Import Dependencies
from pathlib import Path
from dataclasses import dataclass

# Data Ingestion Config
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    dataset_url: str
    dataset_raw: Path

# Data Validation Config
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    dataset_path: Path
    status_file: str

# Base Model Config
@dataclass(frozen=True)
class BaseModelConfig:
    root_dir: Path
    base_model: Path
    model_save: Path
    weights: str
    include_top: bool
    image_size: list

# Model Finetuning Config
@dataclass(frozen=True)
class ModelFinetuneConfig:
    root_dir: Path
    base_model: Path
    model_weights: Path
    train_data: Path
    target_size: list
    learning_rate: float
    epochs: int
    batch_size: int