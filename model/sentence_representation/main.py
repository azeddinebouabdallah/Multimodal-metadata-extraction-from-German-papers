import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import numpy as np

torch.manual_seed(1)

class BLSTM(): 
    # This NLP part Will consist of two bidirectional lstm layers and it's output is 
    # determined by the LSTM's last hidden states or output vectors.

    # This will take as an input a sequence of words and output the last hidden layer
    # the last hidden states of 2-layer bidirectional LSTM will be the input of the last multimodel network 

    def __init__(self, input_dim, hidden_dim,layer_dim, output_dim):
        super(BLSTM, self).__init__()

        #Hidden dimensions
        self.hidden_dim = hidden_dim # maybe set this to 256

        # Number of hidden layers
        self.layer_dim = layer_dim

        # Building the LSTM 
        # batch_first = True causes the input/output to be of shape (batch_dim, seq_dim, feature_dim)
        self.lstm1 = nn.LSTM(input_dim, hidden_dim, layer_dim, batch_first=True, bidirectional=True)


    
    def forward(self, x):
        # Initialize hidden state with zeros

        # self.layer_dim * 2. because we have one going forwards and another going backwards
        h0 = torch.zeros(self.layer_dim * 2, x.size(0), self.hidden_dim)

        # Initialize cell state
        c0 =  torch.zeros(self.layer_dim, x.size(0), self.hidden_dim)

        # We suppose we are conducting a 28 time steps In case of using 
        # We need to detach as we are doing truncated backpropagation through time (BPTT)
        # If we don't, we'll backprop all the way to the start even after going through another batch
        out, (hn, cn) = self.lstm1(x, (h0.detach(), c0.detach()))

        # Index hidden state of last time step
        # out.size() --> 256, 28, 256 if we have (input dim = 28 and hidden dim = 100)
        # out[:, -1, :] => 256, 256 --> because we just want the last time step hidden states
        out = out[:, -1, :] # without an activation function

        # now our: out.size() --> 256, 10 (if output dimension is equal to 10)
        return out




if __name__ == "__main__":

    file = open('test.cermtxt', 'r')
    content = file.read()

    # Pre-processing the text

    # remove the periods 
    # lowercase all text
    content = content.replace('.', '').lower()

    # In form of a list
    words = np.array(content.split())

    # I think words should be in form of a vector.
    


    print(words)