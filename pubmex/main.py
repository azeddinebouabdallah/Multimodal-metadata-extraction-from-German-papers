import torch
from pubmexinference import *
from torchsummary import summary

def main():
    ## Test the model
    pubmex = PubMexInference(
	model_dump="../vision_model/pubmex_model.pth",
	config_file="configs/train_config.yaml",
	use_cuda=False,
    )
    _, metadata, roi_input = pubmex.predict("../ssoar_downloads/niehaus_et_al-gestandnismotivierung_in_beschuldigtenvernehmungen-ocr.pdf")
    print(roi_input)


if __name__ == '__main__':
    main()