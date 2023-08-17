from ChickenDiseaseClassifier.config.configuration import ConfigurationManager
from ChickenDiseaseClassifier.components.data_ingestion import DataIngestion
from ChickenDiseaseClassifier import logger



STAGE_NAME= 'Data Ingestion Stage'


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def run(self):
        config= ConfigurationManager()
        data_ingestion_config= config.get_data_ingestion_config()
        data_ingestion= DataIngestion(
            data_ingestion_config
        )
        data_ingestion.copy_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try: 
        logger.info(f'{">"*5}\t stage: {STAGE_NAME} started. \t{">"*5}')
        obj= DataIngestionTrainingPipeline()
        obj.run()
        logger.info(f'{">"*5}\t stage: {STAGE_NAME} completed. \t{">"*5}')
    except Exception as e:
        # logger.error(f'{">"*5}\t stage: {STAGE_NAME} failed. \t{">"*5}')
        logger.exception(e)