Lesk.py:

Simplified Lesk algorithm to determine the best sence for each instance of a target word. As input, it accepts (1) test sentences file, (2) a sense definition file, and
(3) stop-word file. 

Execution: python test.txt definitions.txt stopwords.txt

(1):
The test sentences file will consist ofsentences, where each sentence contains an instance of the target wordthat needs tobe disambiguated.  The sentences are separated by 
aline-break "\n". Each occurrence  of  the  target  word will  be a  single  word  and  enclosed in brackets  like  this: "<occurrence>WORD</>".  You may find different 
morphological variants of the target word, but all occurrences will have the same root. 
For example,if the target word is “line”, you may find both “line”and“lines” labeled as 
occurrences of “line”. 
For example, the test sentences file for the target word “line” might look likethis: 
Just say the <occurrence>lines</> flat without those curlicues.
Canadians use the North American " qwerty " keyboard , named for the sequence of keys on the top <occurrence>line</> of letters .
In  Houston ,  <occurrence>lines</>  of familieswrapped  around  the  shopping  mall  that houses the legalization center.

(2):
The sense definitions file:
will contain all possible senses for the target word. Each sense will be accompanied bya definition and an example sentence thatare each separated
by a tab "\t". Each line of thefile will havethe following format: 
<sense>\t<one definition sentence>\t<one example sentence>
For example, an entry for one sense ofthe target word "line"could be: 
phone a telephone connection  the line went deadwhere "phone"is the sensename, "a telephone connection"is the sense’s definition and "the line wentdead"is the example sentencefor the phone sense. 


(3):
Stopwords File:
The stopwords file will contain a list of stopwords, each separated by a line break"\n".

Output: Your  programshouldproducean  output  filewith  the  same  name  as  the  test  sentences files but ending with the suffix “.lesk” (e.g., test.txt.lesk). The output file shouldcontain the sense rankingsfor each occurrence of the target word in the test sentences file. Each line of the output file should bearanked list of senses for a test instance,in the order of decreasing overlap scores,from left to right.Printeach sense with its score in parentheses. For example, the outputfor a test instance of the target word "line"mightlook likethis:
text(4)phone(3)product(2)cord(0)division(0)formation(0)
where "text"is the highest rankedsense with an overlap score of"4",and "formation"is thelowest ranked sense with an overlapscore of "0".  


PART 2: Nearest-neighbor Algorithm

For  the  second  part  of  the  assignment,you will  implement nearest-neighbormatchingusing distributional similarity. This method willselectthe best sense foran instance of a target word in a sentence based onthe cosine similarity between each sense’ssignature vectorand a context vector constructed from the sentence.Your program should accept fourarguments: (1)aTraining Sentencesfile, (2)a Test Sentences file, (3) a Stopwords file, and (4) a parameter kforthe context window size. Your program should be named “distsim” and should accept thesearguments on the command-line in the order above. For example, we should be able to run your program like so:

python3  distsim.py train.txt test.txt stopwords.txt 2


**Training and Test Sentences Files**
The Test Sentences file will have exactly the same format as in PART 1. The Training Sentences file will be similar, except that each sentence will be preceded by “GOLDSENSE:<goldsense>\t”, where “goldsense” is the correct sense for the target word in the given sentence. We will refer to the  gold  sense  and  its  corresponding  sentence  as  a  training  instance.  For  example,  a  training instance might look like this: GOLDSENSE:product Mr.  Mottus  added  that  Noxell  may  have  been  "  spoiled  by  "  the success of its Cover Girl <occurrence>line</> .
  
  
**Stopwords File and k Parameter:**
The Stopwords file will have the same format as in PART 1. The kparameter will beanon-negative integer representing the size of the context window to use around  the target  word occurrence. The  context  vector  should  be  constructed  from kwords immediately tothe left of the target word andkwords immediately to its right. Special case:if k=0, use the entire sentence as the context window for the target word.

**Nearest Neighbor Matching Algorithm **

Training
1.You should collect all of the distinct terms that appear in the training sentences filewithin the context window kof a target word occurrence. For example, if k=2 then collect all of the  words  that  appear  within  2  words  on  the  left side  and  2  words  on  the right  side  of  a target word occurrence. Words should be treated as case insensitive, so for example “dog” and “Dog” are considered to be the same term. You should then discard all terms that are stop words, have noalphabetical letters, or have a frequency count of 1. The remaining terms will beyour vocabulary (V). 

2.You should collect all of the distinct gold senses in the training sentences file. This set will beyour sense inventory for the target word.

3.For each gold sense si, you should create a signature vectorfor that sense. To createthis vector, collect all of the sentences that contain instances of the target word labeled as siand extract the contexts around each occurrence of thetarget word based on the window size k. Then create a vector of size |V| where each position of the vector represents a word in your vocabulary. The value for each vocabulary term should beits total frequency count in the collection of contexts for sense si. NOTE: some words that appear in a context window may not be in your vocabulary (e.g., stopwords and words without alphabetic letters). They are still part of the context window, but they will not be used in the signature vector.

**Testing**
1. Given an instance of a target word in a sentence, create a context vector for the word using window size k.  The context vector should have size |V| and usethe same vocabulary and word indices as the signature vectors. Any words in the context windowthat are not in the vocabulary  will  not  be  used  in  the  signature  vector.The  value  for  a  word  should  be  its frequency in the context window.

2.Compute the cosine similarity between the context vector and each of the signature vectors for  the  gold  senses.  The  sense  whose  signature  vector  has  the  highest  cosine  similarity score is the predicted sense. If the denominator of the cosine equation is zero, then set the cosine score to be zero 



**Output:Your programshouldproducean output file with the same name as the test sentences file but ending with the suffix “.distsim”** (e.g., test.txt.distsim). 
The first four lines of the output file should print statistics about the input files as follows:
**Number of Training Sentences = #
Number of Test Sentences = #
Number of Gold Senses = #
Vocabulary Size = #**


Each subsequent line of the output file should be a ranked list of senses for a test instance, printed in order of decreasing cosine similarity scores,from left to right. Print each sense with its cosine score in parentheses, with exactly 2 significant digits after the decimal point using rounding. For example, the outputfor an instanceof the target word "line"mightlook likethis:
              **text(0.81)phone(0.72)product(0.70)cord(0.33)division(0.15)formation(0.00)**
If there  is  a  tie,  you  should  break  the  tie based  onalphabetical  order,  so  thatthe  sense  with  the smaller string value is ranked higher.Be  sure  that  the  lines  in  the  output  file correspond  to  the  same  ordering  of  target  word occurrences in the test sentences file!For example, the first line in the output file should have the sense rankings for the first word occurrence in the test sentences file, the second line in the output file should correspond to the second word occurrence in the test sentences file, etc.
