from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingeation_pipeline import DataIngeationTrainingipeline
from src.textSummarizer.pipeline.stage_2_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataIngeationTrainingipeline()
    data_ingestion_pipeline.initiate_data_ingeation()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e 