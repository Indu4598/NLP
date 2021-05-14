How to run?
- Create a virtual env . 
- unzip the folder contents into that which has QA, models.py, constant.py and QA-script.txt
- run `chmod +x QA-script.txt` to make an executable
- run `./script.txt` to install all the required packages
- run the program using `python3 QA inputfile`
- the program creates the response file in the directory whose path is given in the inputfile


a) For reference, following are the packages that are required. <br/>
pip install -U spacy <br/>
pip install -U textblob <br/>
pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html <br/>
pip install --user -U nltk <br/>
mkdir fastText <br/>
curl -Lo fastText/crawl-300d-2M.vec.zip https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M.vec.zip <br/>
unzip fastText/crawl-300d-2M.vec.zip -d fastText/ <br/>
mkdir encoder <br/>
curl -Lo encoder/infersent2.pkl https://dl.fbaipublicfiles.com/infersent/infersent2.pkl <br/>

b) One document takes approximately takes 7.8 seconds <br/>
