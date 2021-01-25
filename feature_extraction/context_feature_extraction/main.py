from elmoformanylangs import Embedder
import pickle
from conllu import parse # consider using parse incr

import pandas as pd

import numpy as np
import pandas as pd

class ContextFeatureExtractor:
    
    def __init__(self):
        self.i = 0

    def word_embedding(self, conllu_location, output_location):

            
        with open(conllu_location, 'rb') as file:
            words_list = pickle.load(file)
            file.close()

        embedder = Embedder('./de.model')

        feature_vectors = embedder.sents2elmo(words_list)

        feature_vectors = np.array(feature_vectors)

        print(feature_vectors.shape)

        # concatinate layout features and context 
        layout_features_csv = pd.read_csv('../layout_feature_extraction/feature_vectors/document0vectors.csv')

        layout_features = np.array(layout_features_csv)


        feature_vectors = np.concatenate((layout_features, feature_vectors.reshape(feature_vectors.shape[0], -1)), axis=1)

        df = pd.DataFrame(data=feature_vectors)
        df.to_csv('feature_vector.csv')

        with open(output_location, 'wb') as handle:
            pickle.dump(feature_vectors, handle, protocol=pickle.HIGHEST_PROTOCOL)
            handle.close()
            


if __name__ == "__main__":
    contextExtractor = ContextFeatureExtractor()
    contextExtractor.word_embedding('document0.pickle', 'document_vector.pickle')
