import sys
import os
from numpy import *
import re

test = sys.argv[1]
definition = sys.argv[2]
stop = sys.argv[3]

test_head,test_tail=os.path.split(test)


test_file=open(test,"r")
definition_file=open(definition,"r")
stop_file=open(stop,"r")

stop_words=set()
for f in stop_file:
    stop_words.add(f.split()[0])

def not_alpha(s):
    count=0
    for  i in s:
        if i.isalpha():
            count+=1

    if len(s)-count==len(s):
        return 1
    else:
        return 0



freq_dict={}
def remove(s):
    word_list=[]
    for i in s:
        if not_alpha(i) :
            continue
        elif re.search("<occurrence>.*</>", i):
            continue
        else:
            word_list.append(i.lower())

    word_list_set=set(word_list)
    return word_list_set-stop_words

def_dict={}
def_words_list=[]
for f in definition_file:
    def_words=f.split()
    word=def_words[0]
    def_dict[word]=None
    def_words_list=[]
    def_words.remove(def_words[0])
    for i in def_words:
        if not_alpha(i):
            continue
        else:
            def_words_list.append(i.lower())
    def_words_set=set(def_words_list)-stop_words
    def_dict[word]=def_words_set


def overlap(signature, context):
    overlap_dict={}
    for key,value in signature.items():

        temp_set=set()

        temp_set = value & context


        overlap_dict[key] = len(temp_set)

    sorted_d = dict(sorted(overlap_dict.items(), key=lambda x: (-x[1],x[0])))
    return sorted_d
    # for key, value in sorted_d.items():
    #     print("%s(%d) " % (key, value), end=" ")
    # print()

out_test=test_tail+".lesk"
f2=open(out_test,"w")


for f in test_file:
    context=f.split()
    context=remove(context)
    final_dict=overlap(def_dict,context)

    for key,value in final_dict.items():
        s=""
        s=s+key
        s=s+"("
        s=s+str(value)
        s=s+")"
        s=s+" "
        f2.write(s)
    f2.write("\n")



