import torch
from pubmexinference import *
from torchsummary import summary
import pdb

def main():
    ## Test the model
    pubmex = PubMexInference(
	model_dump="vision_model/model_final.pth",
	config_file="configs/train_config.yaml",
	use_cuda=False,
    )

    _, metadata, hidden_layer_output = pubmex.predict("../../ssoar_downloads/niehaus_et_al-gestandnismotivierung_in_beschuldigtenvernehmungen-ocr.pdf")

    ## I'm not sure, which tensor we should use. But I think we should use the latest output which came from the predictor layer 
    ##  I store it in hidden_layer_output['pre_out']


    # print(hidden_layer_output) 
    # pdb.set_trace()

if __name__ == '__main__':
    main()