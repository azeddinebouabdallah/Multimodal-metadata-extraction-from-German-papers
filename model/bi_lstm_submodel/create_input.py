import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from sklearn.model_selection import train_test_split
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
from torch.utils.data import Dataset, DataLoader

import numpy as np
import pandas as pd
import pickle
import random
import os


# Reading the features NOTE: Do not run this it is already saved under vectors.pickle
i = 0
batch_size=128
batch_i = 1

vectors = np.array([])
labels = np.array([])
for file in os.scandir('../../feature_extraction/features/'):
    if file.name.endswith('csv'):
        vector = pd.read_csv(file)
        if (vector.shape[1] == 1044 or vector.shape[1] == 1047):
            # Some files have issues
            continue
        elif (vector.shape[1] == 1046):
            # Some files have an unnecessary column
            vector.drop([vector.columns[0]], axis=1, inplace=True)
        if i == 0:
            vectors = vector.to_numpy()
        else: 
            vectors = np.concatenate((vectors, vector.to_numpy()))
        i+=1
        print(i, end="\r")
        
        
        if i % batch_size == 0: 
            file_name = "./model_inputs/batch"+str(batch_i)+'.pickle'
            with open(file_name, "wb") as f:
                pickle.dump(vectors, f)
            vectors = np.array([])
            i = 0
            batch_i += 1