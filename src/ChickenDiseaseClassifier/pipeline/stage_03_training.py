from ChickenDiseaseClassifier.components.model_trainer import Training
from ChickenDiseaseClassifier.components.prepare_callbacks import PrepareCallback
from ChickenDiseaseClassifier.config.configuration import ConfigurationManager
from ChickenDiseaseClassifier import logger


STAGE_NAME = 'Model Training'

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        logger.info(STAGE_NAME)
        config= ConfigurationManager()
        prepare_callbacks_config= config.get_prepare_callbacks_config()
        prepare_callbacks= PrepareCallback(
            config=prepare_callbacks_config
        )
        callback_list= prepare_callbacks.get_tb_ckpt_callbacks()


        training_config= config.get_training_config()
        training= Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callbacks_list=callback_list
        )


if __name__ == '__main__':
    try: 
        logger.info(f'{">"*5}\t stage: {STAGE_NAME} started. \t{">"*5}')
        obj= ModelTrainingPipeline()
        obj.run()
        logger.info(f'{">"*5}\t stage: {STAGE_NAME} completed. \t{">"*5}')
    except Exception as e:
        # logger.error(f'{">"*5}\t stage: {STAGE_NAME} failed. \t{">"*5}')
        logger.exception(e)