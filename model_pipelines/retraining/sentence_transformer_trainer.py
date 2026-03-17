from sentence_transformers import losses, SentencesDataset
from torch.utils.data import DataLoader
from datetime import datetime

class SentenceTransformerTrainer:
    def __init__(self, dataset, model):
        self.dataset = dataset
        self.model = model

    def train_model(self):
        date_str = datetime.now().strftime("%Y%m%d")

        output_path = f"data/models/solvedesk_sentence_{date_str}"

        train_dataset = SentencesDataset(self.dataset, self.model)
        train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=16)
        train_loss = losses.CosineSimilarityLoss(self.model)

        self.model.fit(
            train_objectives=[(train_dataloader, train_loss)],
            epochs=5,
            warmup_steps=100,
            output_path=output_path
        )

