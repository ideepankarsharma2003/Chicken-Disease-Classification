from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline
from ChickenDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from ChickenDiseaseClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from ChickenDiseaseClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline









STAGE_NAME= 'Data Ingestion Stage'
try: 
    logger.info(f'{">"*5}\t stage: {STAGE_NAME} started. \t{">"*5}')
    obj= DataIngestionTrainingPipeline()
    obj.run()
    logger.info(f'{">"*5}\t stage: {STAGE_NAME} completed. \t{">"*5}')
except Exception as e:
    # logger.error(f'{">"*5}\t stage: {STAGE_NAME} failed. \t{">"*5}')
    logger.exception(e)
    raise e







STAGE_NAME= 'Prepare Base Model'
try: 
    logger.info(f'{">"*5}\t stage: {STAGE_NAME} started. \t{">"*5}')
    obj= PrepareBaseModelTrainingPipeline()
    obj.run()
    logger.info(f'{">"*5}\t stage: {STAGE_NAME} completed. \t{">"*5}')
except Exception as e:
    # logger.error(f'{">"*5}\t stage: {STAGE_NAME} failed. \t{">"*5}')
    logger.exception(e)
    raise e






STAGE_NAME= 'Model Training'
try: 
    logger.info(f'{">"*5}\t stage: {STAGE_NAME} started. \t{">"*5}')
    obj= ModelTrainingPipeline()
    # obj.run()
    logger.info('Model Training p comment mara hai, check kr lena')
    logger.info(f'{">"*5}\t stage: {STAGE_NAME} completed. \t{">"*5}')
except Exception as e:
    # logger.error(f'{">"*5}\t stage: {STAGE_NAME} failed. \t{">"*5}')
    logger.exception(e)
    raise e




STAGE_NAME= 'Model Evaluation'
try: 
    logger.info(f'{">"*5}\t stage: {STAGE_NAME} started. \t{">"*5}')
    obj= ModelEvaluationPipeline()
    # obj.run()
    logger.info(f'{">"*5}\t stage: {STAGE_NAME} completed. \t{">"*5}')
except Exception as e:
    # logger.error(f'{">"*5}\t stage: {STAGE_NAME} failed. \t{">"*5}')
    logger.exception(e)
    raise e