from pubmexinference import *
from tqdm import tqdm # Just for progress bar
from pathlib import Path
from torchsummary import summary
import torch
import pdb
import os
import numpy as np
import pickle as pkl

def main():
    ## Test the model
    pubmex = PubMexInference(
	model_dump="vision_model/model_final.pth",
	config_file="configs/train_config.yaml",
	use_cuda=False,
    )

    pdf_list = []
    
    for file in os.scandir('../../ssoar_dataset/'):
        if file.name.endswith('pdf'):
            pdf_list.append(file.name)


    Path('vision_output2/').mkdir(parents=True, exist_ok=True)

    for pdf in tqdm(pdf_list):
        print("Current File : {0}".format(pdf))
        if os.path.exists('vision_output2/{0}'.format(pdf).split('.')[0] + '.pickle'):
            continue

        predict = pubmex.alt_predict('../../ssoar_dataset/{0}'.format(pdf))

        with open('vision_output2/{0}'.format(pdf).split('.')[0] + '.pickle', 'wb') as handle:
            pkl.dump(predict, handle, protocol=pkl.HIGHEST_PROTOCOL)
            handle.close()




    ## Get score for each instance
    # predict = pubmex.alt_predict("../../ssoar_downloads/niehaus_et_al-gestandnismotivierung_in_beschuldigtenvernehmungen-ocr.pdf")
    # print(predict)


if __name__ == '__main__':
    main()