import os
from ChickenDiseaseClassifier.constants import *
from ChickenDiseaseClassifier.utils.common import read_yaml, create_directories
from ChickenDiseaseClassifier.entity.config_entity import (
                                                            DataIngestionConfig, 
                                                            PrepareBaseModelConfig,
                                                            PrepareCallbacksConfig,
                                                            TrainingConfig,
                                                            EvaluationConfig
                                                        )

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
    



    


    # prepare callbacks config
    def get_prepare_callbacks_config(self) -> PrepareCallbacksConfig:
        config= self.config.prepare_callbacks
        model_ckpt_dir= os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir),
            ])
        
        prepare_callbacks_config= PrepareCallbacksConfig(
            root_dir= Path(config.prepare_callbacks_root),
            checkpoint_model_filepath= Path(config.checkpoint_model_filepath),
            tensorboard_root_log_dir= Path(config.tensorboard_root_log_dir)
        )
        return prepare_callbacks_config
    


    
    # model trainer config
    def get_training_config(self):
        training= self.config.training
        prepare_base_model= self.config.prepare_base_model
        params= self.params
        training_data= os.path.join(
            self.config.data_ingestion.unzip_dir, 'Chicken-fecal-images'
        )
        create_directories([
            Path(training.root_dir)
        ])

        training_config= TrainingConfig(
            root_dir= Path(training.root_dir),
            trained_model_path= Path(training.trained_model_path),
            training_data= Path(training_data),
            updated_model_path= Path(prepare_base_model.updated_base_model_path),
            params_image_size=params.IMAGE_SIZE,
            params_batch_size=params.BATCH_SIZE,
            params_epochs= params.EPOCHS,
            params_is_augmentation=params.AUGUMENTATION,
        )

        return training_config
    




    

    # evaluation config
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config= EvaluationConfig(
            path= Path("artifacts/training/model.h5"),
            training_data= Path("artifacts/data_ingestion/Chicken-fecal-images/"),
            all_parameters= self.params,
            params_image_size= self.params.IMAGE_SIZE,
            params_batch_size= self.params.BATCH_SIZE,
            
        )
        return eval_config
        
