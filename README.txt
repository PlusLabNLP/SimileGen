SET UP ENVIRONMENT
=======================
conda create --name simile python=3.6

conda activate simile

#point your LD_LIBRARY_PATH to your miniconda or anaconda library

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nas/home/miniconda3/lib/


install nltk

SET UP COMET
=======================

cd comet-commonsense

To run the setup scripts to acquire the pretrained model files from OpenAI, as well as the ATOMIC and ConceptNet datasets

bash scripts/setup/get_atomic_data.sh
bash scripts/setup/get_conceptnet_data.sh
bash scripts/setup/get_model_files.sh
Then install dependencies (assuming you already have Python 3.6 ):

pip install torch==1.3.1
pip install tensorflow
pip install ftfy==5.1
conda install -c conda-forge spacy
python -m spacy download en
pip install tensorboardX
pip install tqdm
pip install pandas
pip install ipython
pip install inflect
pip install pattern
pip install pyyaml==5.1
pip install regex==2018.2.21
pip install pytorch_pretrained_bert==0.6.0

Making the Data Loaders
Run the following scripts to pre-initialize a data loader for ATOMIC or ConceptNet:

python scripts/data/make_atomic_data_loader.py
python scripts/data/make_conceptnet_data_loader.py
Download pretrained COMET
First, download the pretrained models from the following link:

https://drive.google.com/open?id=1FccEsYPUHnjzmX-Y5vjCBeyRt1pLo8FB
Then untar the file:

tar -xvzf pretrained_models.tar.gz

SET UP DATA PROCESSING FOR SIMILE
==================================

python scrape_reddit_for_similes.py #Scrapes self labeled similes
python convert_to_literal.py #Converts simile to literal


FINETUNE BART
==================================

Use data from previous step for fine-tuning BART
Sample data in simile folder (train.source --> LITERAL , train.target---> SIMILE)

Use the encoder.json and dict.txt already provided as a part of the repo, since it contains additional delimeter tokens relevant for simile generations


Now for BPE preprocess:
sh create_bpe.sh


Binarize dataset:

sh preprocess.sh


Download Pretrained BART from here:

https://github.com/pytorch/fairseq/tree/4b986c51ed89f9895df2f30e57909301b4a4f19b/examples/bart

Train models:

sh finetune.sh

Update the field BART_PATH to suit where your pretained model.pt file is You can customize MAX_TOKENS and UPDATE_FREQ based on gpu memory / no of gpus

For Inference:

See sample test data in literal.txt
Output will be in simile.hypo

We also included outputs by all system of 10 literal inputs in literal.txt in human_labels.csv.
The auto eval script is also available

python generate.py
