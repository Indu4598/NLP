import sys
import os
import numpy as np
import re
from numpy.linalg import norm


train= sys.argv[1]
test = sys.argv[2]

stop = sys.argv[3]
k = int(sys.argv[4])

train_head,train_tail = os.path.split(train)
test_head,test_tail = os.path.split(test)

f1=open(train,"r")

def not_alpha(s):
    count=0
    for  i in s:
        if i.isalpha():
            count+=1

    if len(s)-count==len(s):
        return 1
    else:
        return 0


stop_words=set()
stop_file=open(stop,"r")
for f in stop_file:
    stop_words.add(f.split()[0])


#part-1 get the vocab and sense inventory
target_word="<occurence>*</>"

sense_inventory=set()
f1=open(train,"r")
vocab=[]
num_train=0
for f in f1:
    train_sentence=f.split()
    gold_sense = train_sentence[0].split(":")
    sense_inventory.add(gold_sense[1])
    words=train_sentence[1:]
    words= [s.lower() for s in words]
    for i,e in enumerate(words):

        if re.search("<occurrence>.*</>",e):
            if k==0:
                vocab.extend(words[0:i])
                vocab.extend(words[i+1:])
            else:
                for j in range(1,k+1):
                    if i==0:
                        break
                    if i - j == 0:
                        vocab.append(words[i - j])
                        break
                    vocab.append(words[i - j])
                for j in range(1,k+1):
                    if i==len(words)-1:
                        break
                    if j + i == len(words) - 1:
                        vocab.append(words[i + j])
                        break
                    vocab.append(words[i + j])


            break
    num_train+=1
f1.close()


vocab_freq={}
for s in vocab:
    if s in vocab_freq:
        vocab_freq[s]+=1
    else:
        vocab_freq[s]=1


temp_vocab1=[]
for s in vocab:
    if not_alpha(s):
        continue
    elif s in stop_words:
        continue
    elif vocab_freq[s]<2:
        continue
    else:
        temp_vocab1.append(s)

vocab_set= set(temp_vocab1)
vocab_list = sorted(list(vocab_set))
# print(vocab_list[0:20])

# Create Signature Vector for all the gold sense:
sense_sig_vec={}
sense_sig_word={}
for w in sense_inventory:
    sense_sig_vec[w] = [0 for i in range(len(vocab_set))]
    sense_sig_word[w]= ['' for i in range(len(vocab_set))]



def get_context(words,k):
    vocab=[]
    words = [s.lower() for s in words]

    for i,e in enumerate(words):
        if re.search("<occurrence>.*</>",e):
            if k==0:
                vocab.extend(words[0:i])
                vocab.extend(words[i+1:])
            else:
                for j in range(1,k+1):
                    if i==0:
                        break
                    if i - j == 0:
                        vocab.append(words[i - j])
                        break
                    vocab.append(words[i - j])
                for j in range(1,k+1):
                    if i==len(words)-1:
                        break
                    if j + i == len(words) - 1:
                        vocab.append(words[i + j])
                        break
                    vocab.append(words[i + j])

    return vocab


f1=open(train,"r")
for f in f1:
    comp_sentence = f.split()
    sense_word=comp_sentence[0].split(':')[1]
    sen=comp_sentence[1:]
    temp_list = get_context(sen,k)

    for w in temp_list:
        if w in vocab_list:
            ind = vocab_list.index(w)
            sense_sig_vec[sense_word][ind]+=1

# for key,values in sense_sig_vec.items():
#     print(key,norm(sense_sig_vec[key]))
out_test=test_tail+".distsim"
f3=open(out_test,"w")

num_test=0
f2 =open(test,'r')
for f in f2:
    num_test+=1
f2.close()



f3.write("Number of Training Sentences = ")
f3.write(str(num_train))
f3.write("\n")
f3.write("Number of Test Sentences = ")
f3.write(str(num_test))
f3.write("\n")
f3.write("Number of Gold Senses = ")
f3.write(str(len(sense_sig_vec.keys())))
f3.write("\n")
f3.write("Vocabulary Size = ")
f3.write(str(len(vocab_list)))
f3.write("\n")


f2 =open(test,'r')
test_sen=0
for f in f2:
    test_words=f.split()

    temp_test = get_context(test_words,k)
    temp_dict={}
    temp1=[0 for i in range(len(vocab_list))]
    temp_dict={}
    for w in temp_test:
        if w not in temp_dict:
            temp_dict[w]=1
        else:
            temp_dict[w]+=1


    for w in temp_test:
        if w in vocab_list:
            ind = vocab_list.index(w)
            temp1[ind]=temp_dict[w]

    norm_dict={}
    for key, values in sense_sig_vec.items():
        temp2=sense_sig_vec[key]
        dot_pro=np.dot(temp1,temp2)
        norm_d=norm(temp1)*norm(temp2)

        if norm_d == 0:
           norm_dict[key] = float(0.00)
        else:
           norm_dict[key]=dot_pro/norm_d

    norm_dict= dict(sorted(norm_dict.items(), key=lambda x: (-x[1], x[0])))

    for key, values in norm_dict.items():
        norm_dict[key]=round(norm_dict[key],2)

    for key, values in norm_dict.items():
        f3.write(key)
        f3.write("(")
        f3.write(str(values))
        f3.write(")")
        f3.write(" ")
    f3.write("\n")












