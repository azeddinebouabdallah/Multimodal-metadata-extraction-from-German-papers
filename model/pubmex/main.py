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

    ## In case you want to get output instaed
    ##      Change self.model.roi_heads.mask_head.register_forward_pre_hook(get_roi_heads_input) in prediction.py to self.model.roi_heads.mask_head.register_forward_hook(get_roi_heads_input), then add 1 more argument in get_roi_heads_input function
    ##      If you want to see the entire architecture of the model, you can uncomment pdb.settrace() in __call__ function of Prediction class and print the model
    
    _, metadata, roi_input = pubmex.predict("../ssoar_downloads/niehaus_et_al-gestandnismotivierung_in_beschuldigtenvernehmungen-ocr.pdf")
    print(roi_input)


if __name__ == '__main__':
    main()