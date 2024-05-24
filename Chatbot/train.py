import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from utils import load_data, preprocess_data
from model import ChatModel

class ChatDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

def train_model(json_file, num_epochs=1000, learning_rate=0.001, hidden_size=8, batch_size=8):
    data = load_data(json_file)
    X, y, all_words, tag_list = preprocess_data(data)

    input_size = len(all_words)
    output_size = len(tag_list)
    dataset = ChatDataset(X, y)
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)

    model = ChatModel(input_size, hidden_size, output_size)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        for (inputs, labels) in train_loader:
            inputs = inputs.to(torch.float32)
            labels = labels.to(torch.long)

            outputs = model(inputs)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    torch.save(model.state_dict(), "chat_model.pth")
    print('Model training complete. Model saved to "chat_model.pth".')

    return model, all_words, tag_list

if __name__ == "__main__":
    train_model('intents.json')