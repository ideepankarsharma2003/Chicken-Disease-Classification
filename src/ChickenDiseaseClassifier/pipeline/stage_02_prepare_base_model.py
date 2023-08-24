from ChickenDiseaseClassifier.components.prepare_base_model import PrepareBaseModel
from ChickenDiseaseClassifier.config.configuration import ConfigurationManager
from ChickenDiseaseClassifier import logger


STAGE_NAME = 'Prepare base model'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        logger.info(STAGE_NAME)
        config= ConfigurationManager()
        prepare_base_model_config= config.get_prepare_model_config()
        prepare_base_model= PrepareBaseModel(
            config= prepare_base_model_config
        )
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()