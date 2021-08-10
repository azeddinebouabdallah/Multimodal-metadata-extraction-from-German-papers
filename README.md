# Multimodal Approach for Metadata Extraction from German Scientific Publications
This repository contains a method to extract metadata from german scientific 
literatures using multimodal approach. By combination of vision and text model

In this project we using [MEXPUB](https://github.com/nbeili/Metadata-extraction-from-German-scientific-papers) for vision model and Bi-LSTM submodel before feed into another Bi-LSTM model.
This model can extract the following meta data : Title, Author, Journal, Abstract, Affiliation, Email, Address, DOI, Date.
## Requirements
Python >= 3.6  
Linux or MacOS
## Installation
1. Clone the repository and install required library
``` 
git clone git@github.com:azeddinebouabdallah/research-lab-ml.git
cd research-lab-ml
pip install -r requirements.txt
pip install torch==1.7.1+cpu torchvision==0.8.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.7/index.html
pip install -U 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'
```
2. Download [the model](https://drive.google.com/file/d/1Ie1SeTKoqzPH86DN2xPBgEz-3qq6DLoE/view?usp=sharing) and move it into "model/pubmex/vision_model/" (Create new folder if not exist)
3. Download [ELMO model](http://vectors.nlpl.eu/repository/11/142.zip) and extract it into "feature_extraction/context_feature_extraction/de.model/"

4. Install [ELMoForManyLangs](https://github.com/HIT-SCIR/ELMoForManyLangs)
```
cd feature_extraction/context_feature_extraction/de.model/ELMoForManyLangs-master   # move into ELMO folder
python setup.py install
```
## Web Application
For running the simple web application, please follow the instruction on [this page](https://github.com/azeddinebouabdallah/Multimodal-metadata-extraction-from-German-papers/tree/master/web_application_demo/metadata_extraction_web)
