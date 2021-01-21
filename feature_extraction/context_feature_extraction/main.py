from elmoformanylangs import Embedder
import pickle

import numpy as np
import pandas as pd

class ContextFeatureExtractor:
    
    def __init__(self):
        self.i = 0

    def word_embedding(self, pickle_location, output_location):

        with open(pickle_location, 'rb') as file:
            words_list = pickle.load(file)
            file.close()

        embedder = Embedder('./de.model')

        feature_vectors = embedder.sents2elmo(words_list)

        with open(output_location, 'w') as f:
            for item in feature_vectors:
                f.write("%s\n" % item)
            


if __name__ == "__main__":
    contextExtractor = ContextFeatureExtractor()
    contextExtractor.word_embedding('document0.pickle', 'document_vector.txt')