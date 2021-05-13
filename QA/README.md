How to run?
- Create a virtual env on CADE machine. 
- unzip the folder contents into that which has QA, models.py, constant.py and QA-script.txt
- run `chmod +x QA-script.txt` to make an executable
- run `./script.txt` to install all the required packages
- run the program using `python3 QA inputfile`
- the program creates the response file in the directory whose path is given in the inputfile

We tested our program on CADE machine lab1-10.
We frequently ran out of disc space that was alloted to our individual machines and had to delete most of the stuff.

a) For reference, following are the packages that are required.
pip install -U spacy
pip install -U textblob
pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install --user -U nltk
mkdir fastText
curl -Lo fastText/crawl-300d-2M.vec.zip https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M.vec.zip
unzip fastText/crawl-300d-2M.vec.zip -d fastText/
mkdir encoder
curl -Lo encoder/infersent2.pkl https://dl.fbaipublicfiles.com/infersent/infersent2.pkl

b) One document takes approximately takes 7.8 seconds

c) 
   ---Phase 1---
   Parsing the paragraph into individual sentences followed by vector embeddings - Shaurya
   Reading and parsing questions into vectors - Indu
   Getting the cosine similarity for sentence extraction - Indu
   Matching the roots of questions and sentences - Shaurya
   Getting the type of questions and returning answers based on that type - Indu 

   ---Phase 2---
   For the final evaluation, we manually added a bunch of rules. Both of us added approx half of those each. 
   Shaurya refactored the code from midterm submission to make it more readable and maintainable.
   Indu tested the system multiple times.

