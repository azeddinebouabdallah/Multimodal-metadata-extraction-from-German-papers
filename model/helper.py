import pandas as pd
import numpy as np
import os

for file in os.scandir("../feature_extraction/features"):
    if (file.name.endswith(".csv")) and os.path.isfile('../data_generation/generated_annotations/{0}'.format(file.name)):
        df1 = pd.read_csv(file)
        df2 = pd.read_csv('../data_generation/generated_annotations/{0}'.format(file.name))
        df1['Label'] = df2['Label']

