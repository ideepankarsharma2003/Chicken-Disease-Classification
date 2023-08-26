from ChickenDiseaseClassifier.components.model_evaluation import Evaluation
from ChickenDiseaseClassifier.components.prepare_callbacks import PrepareCallback
from ChickenDiseaseClassifier.config.configuration import ConfigurationManager
from ChickenDiseaseClassifier import logger


STAGE_NAME = 'Model Evaluation'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def run(self):
        config= ConfigurationManager()
        eval_config= config.get_evaluation_config()
        evaluation= Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()