Lesk.py:

Simplified Lesk algorithm to determine the best sence for each instance of a target word. As input, it accepts (1) test sentences file, (2) a sense definition file, and
(3) stop-word file. 

Execution: python test.txt definitions.txt stopwords.txt

(1):
The test sentences file will consist ofsentences, where each sentence contains an instance of the target wordthat needs tobe disambiguated.  The sentencesare separated by 
aline-break "\n". Eachoccurrence  of  the  target  word will  bea  single  word  and  enclosed in brackets  like  this: "<occurrence>WORD</>".  You may find different 
morphological variants of the target word, but all occurrences will have the same root. 
For example,if the target word is “line”, you may find both “line”and“lines” labeled as 
occurrencesof “line”. 
For example, the test sentences file for the target word “line” might look likethis: 

** Just say the <occurrence>lines</> flat without those curlicues .
Canadians use the North American " qwerty " keyboard , named for the sequence of keys on the top <occurrence>line</> of letters .
In  Houston ,  <occurrence>lines</>  of familieswrapped  around  the  shopping  mall  that houses the legalization center . **
