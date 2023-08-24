from ChickenDiseaseClassifier.constants import *
from ChickenDiseaseClassifier.utils.common import read_yaml, create_directories
from ChickenDiseaseClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig

class ConfigurationManager:
    def __init__(
            self,
            config_file_path= CONFIG_FILE_PATH,
            params_file_path= PARAMS_FILE_PATH
            ):


        print(f"Loading configuration from {config_file_path}")
        print(f"Loading parameters from {params_file_path}")

        self.config= read_yaml(config_file_path)
        self.params= read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])





    # data ingestion configuration 
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config= self.config.data_ingestion

        create_directories([config.data_ingestion_root])

        data_ingestion_config= DataIngestionConfig(
            root_dir= config.data_ingestion_root,
            source_url=config.source_url,
            local_data_file =config.local_data_file,
            unzip_dir =config.unzip_dir,
        )
        return data_ingestion_config




    # prepare model configuration 
    def get_prepare_model_config(self) -> PrepareBaseModelConfig:
        config= self.config.prepare_base_model
        create_directories([config.prepare_base_model_root])

        prepare_base_model_config= PrepareBaseModelConfig(
            root_dir= Path(config.prepare_base_model_root),
            base_model_path= Path(config.base_model_path),
            updated_base_model_path= Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            # params_batch_size=self.params.BATCH_SIZE,
            params_include_top=self.params.INCLUDE_TOP,
            # params_epochs=self.params.EPOCHS,
            params_classes=self.params.CLASSES,
            params_weights=self.params.WEIGHTS,
            params_learning_rate=self.params.LEARNING_RATE, 

        )
        return prepare_base_model_config