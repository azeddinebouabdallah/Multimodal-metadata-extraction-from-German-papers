# Multimodal Approach for Metadata Extraction from German Scientific Publications
This repository contains a method to extract metadata from german scientific 
literatures using multimodal approach. By combination of vision and text model

In this project we using [MEXPUB](https://github.com/nbeili/Metadata-extraction-from-German-scientific-papers) for vision model and Bi-LSTM submodel before feed into another Bi-LSTM model.
This model can extract the following meta data : Title, Author, Journal, Abstract, Affiliation, Email, Address, DOI, Date.
## Installation

1. Download [the model](https://drive.google.com/file/d/1Ie1SeTKoqzPH86DN2xPBgEz-3qq6DLoE/view?usp=sharing) and move it into "model/pubmex/vision_model/" (Create new folder if not exist)
2. Download [ELMO model](http://vectors.nlpl.eu/repository/11/142.zip) and extract it into "feature_extraction/context_feature_extraction/de.model/"
3. Clone the repository and install required library
``` 
git clone git@github.com:azeddinebouabdallah/research-lab-ml.git
cd research-lab-ml
pip3 install -r requirements.txt
```
4. Install [ELMoForManyLangs](https://github.com/HIT-SCIR/ELMoForManyLangs)
```
mv feature_extraction/context_feature_extraction/de.model/ELMoForManyLangs-master   # move into ELMO folder
python setup.py install
```

## Web Demo
Currently, the sample of our model have been deploy on https://metadata-extraction-web.herokuapp.com/. Which can be use to upload and extract metadata from the first page of pdf
