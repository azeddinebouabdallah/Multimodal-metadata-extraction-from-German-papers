import numpy as np
import pandas as pd
import os
import pickle
import math

def manualAnnotated():
    i = 0 
    for file in os.scandir("../feature_extraction/features/"):
        if file.name.endswith("csv"):
            file_vectors = pd.read_csv(file)
            if (file_vectors.shape[1] == 1044 or file_vectors.shape[1] == 1047):
                # Some files have issues
                continue
            elif (file_vectors.shape[1] == 1046):
                # Some files have an unnecessary column
                file_vectors.drop([file_vectors.columns[0]], axis=1, inplace=True)

            output = file_vectors.iloc[:, [2, -1]]
            output.columns = ["word", "label"]

            new_vectors = np.array([])
            for index, row in output.iterrows():
                if math.isnan(row['label']):
                     continue
                v = np.zeros(10)
                v[int(row['label']) - 1] = 1

                new_vectors = np.append(new_vectors, np.array([row['word'], v]))


            with open("./nlp_output/{0}.pickle".format(file.name.split('.')[0]), "wb") as f:
                pickle.dump(new_vectors, f)
                i+=1
                print("File {0}".format(i), end='\r')
    print("finished processing {0} files".format(i))


if __name__ == "__main__":
    manualAnnotated()
