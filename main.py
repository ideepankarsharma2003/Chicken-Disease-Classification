from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline









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