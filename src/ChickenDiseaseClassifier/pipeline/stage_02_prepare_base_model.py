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
        logger.info(STAGE_NAME+ " loaded config")
        prepare_base_model_config= config.get_prepare_model_config()
        logger.info(STAGE_NAME+ " loaded pbmc ")
        prepare_base_model= PrepareBaseModel(
            config= prepare_base_model_config
        )
        prepare_base_model.get_base_model()
        logger.info(STAGE_NAME+ " got base model")
        prepare_base_model.update_base_model()
        logger.info(STAGE_NAME+ " update base model")



if __name__ == '__main__':
    try: 
        logger.info(f'{">"*5}\t stage: {STAGE_NAME} started. \t{">"*5}')
        obj= PrepareBaseModelTrainingPipeline()
        obj.run()
        logger.info(f'{">"*5}\t stage: {STAGE_NAME} completed. \t{">"*5}')
    except Exception as e:
        # logger.error(f'{">"*5}\t stage: {STAGE_NAME} failed. \t{">"*5}')
        logger.exception(e)