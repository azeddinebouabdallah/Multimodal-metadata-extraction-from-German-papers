# Multimodal Approach for Metadata Extraction from German Scientific Publications Web Demo
This repository contains a simple web application for testing [model](https://github.com/azeddinebouabdallah/research-lab-ml) as a part of research lab.
## Installation

1 Change directory into the folder and install required library by using pip
```
cd research-lab-ml/web_application_demo/metadata_extraction_web/
git clone git@github.com:azeddinebouabdallah/research-lab-ml.git
cd research-lab-ml
pip install -r requirements.txt
pip install torch==1.7.1+cpu torchvision==0.8.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.7/index.html
pip install -U 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'

```
2. Download [ELMO model](http://vectors.nlpl.eu/repository/11/142.zip) and extract it into "feature_extraction/context_feature_extraction/de.model/" and /de.model/
3. Create 3 empty folder
```
mkdir features
mkdir word_lists
mkdir feature_vectors
```
## Running the demo
1. First export flask app environment variable
```
export FLASK_APP=app.py
```
2. Run Flask
```
flask run
```
3. without modification to the flask, this app will be host on localhost port 5000 http://127.0.0.1:5000/
