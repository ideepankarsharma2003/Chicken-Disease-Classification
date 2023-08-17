from ChickenDiseaseClassifier.constants import *
from ChickenDiseaseClassifier.utils.common import read_yaml, create_directories
from ChickenDiseaseClassifier.entity.config_entity import DataIngestionConfig

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