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

    ## Get score for each instance
    predict = pubmex.alt_predict("../../ssoar_downloads/niehaus_et_al-gestandnismotivierung_in_beschuldigtenvernehmungen-ocr.pdf")

    ## Original pubmex
    # v, metadata = pubmex.predict("../../ssoar_downloads/niehaus_et_al-gestandnismotivierung_in_beschuldigtenvernehmungen-ocr.pdf")

    print(predict)
    # pdb.set_trace()


if __name__ == '__main__':
    main()