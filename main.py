from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingeation_pipeline import DataIngeationTrainingipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataIngeationTrainingipeline()
    data_ingestion_pipeline.initiate_data_ingeation()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e 