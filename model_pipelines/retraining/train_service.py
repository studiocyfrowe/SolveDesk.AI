# application/services/train_service.py
from model_pipelines.datasets.dataset_builder import DatasetBuilder
from model_pipelines.retraining.sentence_transformer_trainer import SentenceTransformerTrainer

class TrainService:
    def __init__(self, source, model):
        self.source = source
        self.model = model

    def train(self):
        issues = self.source.fetch()
        builder = DatasetBuilder()
        dataset = builder.build_from_issues(issues)

        trainer = SentenceTransformerTrainer(dataset, self.model)
        return trainer.train_model()