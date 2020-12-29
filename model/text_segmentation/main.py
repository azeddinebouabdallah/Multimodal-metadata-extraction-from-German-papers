import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)

class TextSegentorSentence():

    def __init__(self, num_words, hidden_dim, ):
        self.lstm_1 = nn.LSTM(num_words, num_words)







if __name__ == "__main__":
    print('Run')