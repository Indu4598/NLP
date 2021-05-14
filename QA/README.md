<h1>Question Answering System</h1>

<h3> Aim </h3>
<b>Build a question answering system, that process a story and qustions related to it and produces an answer.</b>

<img src="https://github.com/Indu4598/NLP/blob/master/QA/Architecture.png" width="500" />

<h3>Root Match</h3>
  1. We extracted the root words of the question and each sentences. <br/>
  2. Sentences were rewarded based on the number of common roots it had with the question. <br/>
 
<h3>Word Match</h3>
  1. The sentence was rewarded based on the common words it shared with the question. <br/>
  2. A verb got the sentence 6 points, a proper noun got 1 point and any other word got 3 points. <br/>

<h3>Question Type Classification</h3>
  1. We then extracted the question type and applied corresponding rules for each type of question. <br/>
  2. Sentences which satisfied the rules were again rewarded. <br/>
  
<h3>Rule Based Scoring</h3>
  1. After we determined the question type, we applied rule-based scoring. <br/>
  2. For example, if the question type was where - sentences with clue about position were rewarded. Clues about position included preposition and NER tags like ORG, GPE, and LOC. <br/>

<h3>Answer Extraction</h3>
  1. Based on the cumulative scores of root-match, word-match, and rule-based scoring, the sentence with the highest score was selected as a sentence containing the answer.  <br/>
  2. NER-tagging was then applied on the sentences. Depending upon the classification of the question type words corresponding to the appropriate tags were append to the answer.  <br/>

