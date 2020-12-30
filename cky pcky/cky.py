
import sys
import os



grammar_file = sys.argv[1]
sentence_file = sys.argv[2]









f1=open(grammar_file,"r")
f2=open(sentence_file,"r")

rules=[]
right_rule=[]
left_rule=[]
prob_vals=[]
for f in f1:
    words = f.replace("->", "").split()
    right_rule.append(words[0])
    left_rule.append(words[1:-1])
    prob_vals.append(float(words[-1]))
    rules.append(words)



# print(right_rule)
# print(left_rule)
# print(prob_vals)




def get_NT(s):
    return_list=[]
    for rule in rules:
        if s in rule:
            return_list.append(rule[0])


    return return_list

def get_right(l1,l2):
    res=[]
    for x in l1:
        l1=[]
        l1.append(x)
        for y in l2:
            l1.append(y)
            for i in range(len(left_rule)):
                if l1==left_rule[i]:
                    # print(left_rule[i])
                    # print(right_rule[i])
                    # print(prob_vals[i])
                    res.append(right_rule[i])
            l1.pop(-1)

    return res


def get_right_prob(l1,l2):
    res=[]
    dict_r={}
    for x in l1:
        l1=[]

        l1.append(x)
        for y in l2:
            l1.append(y)
            for i in range(len(left_rule)):
                if l1==left_rule[i]:
                    # print(left_rule[i])
                    # print(right_rule[i])
                    # print(prob_vals[i])
                    # print("*****")
                    dict_r[right_rule[i]]=prob_vals[i]
                    res.append(rules[i])
            l1.pop(-1)
    # print(res)
    return res

def get_rule(l1,l2):
    res = []
    res1=[]
    for x in l1:
        l1 = []
        l1.append(x)
        for y in l2:
            l1.append(y)
            for i in range(len(left_rule)):
                if l1 == left_rule[i]:
                    # print(left_rule[i])
                    # print(right_rule[i])
                    # print(prob_vals[i])
                    res=[]
                    res.append(right_rule[i])
                    res.extend(left_rule[i])
                    res.append(prob_vals[i])
                    res1.append(res)
            l1.pop(-1)
    # print(res1)
    return res1



# get_right_prob(['VERB','VP'],['PP','NP'])

def get_prob(s):
    return_list = []
    temp_dict={}
    for i in range(len(left_rule)):
        if s in left_rule[i]:
            temp_dict[right_rule[i]]=prob_vals[i]

    return temp_dict

# print(get_prob("fish"))




# print(get_right(['DET'],['NOM','NN']))



# def get_right(list_g):
#     if list_g in left_rule:


def cky(s):

    n_words=len(s.split())
    words=s.split()

    table=[]
    #Number of columns
    res = [[[] for x in range(n_words)] for y in range(n_words)]



    for i in range(n_words):
        # print("i-loop",i)
        res[i][i] = get_NT(words[i])


        for j in range(i-1,-1,-1):
            # print("j-loop", j)
            for k in range(j+1,i+1):
                # print("k-loop",k)
                temp=[]
                B=[]
                C=[]
                B.extend(res[j][k-1])
                C.extend(res[k][i])
                # print(B)
                # print(C)
                temp=get_right(B,C)
                res[j][i].extend(temp)
                ##get_right(B,C)
                # print(i, j, res[j][i])
                # print("*******")


    print("PARSING SENTENCE:",s)
    n_prases=res[0][n_words-1].count('S')
    print("NUMBER OF PARSES FOUND: ",n_prases)
    print("TABLE:")
    for i in range(n_words):
        for j in range(n_words):
            if i<=j:
                print("cell[%d,%d]: "%(i+1,j+1),end="")
                if res[i][j]!=[]:
                    for x in sorted(res[i][j]):
                        print(x, end=" ")
                else:
                    print('-',end="")
                print()



def pcky(s):

    n_words=len(s.split())
    words=s.split()

    table=[]
    #Number of columns
    res = [[{} for x in range(n_words)] for y in range(n_words)]
    prob=[[0 for x in range(n_words)] for y in range(n_words)]


    for i in range(n_words):
        # print("i-loop",i)
        res[i][i] = get_prob(words[i])


        # print(res[i][i]['S'])


        for j in range(i-1,-1,-1):

            for k in range(j+1,i+1):

                B=list(res[j][k-1].keys())
                C=list(res[k][i].keys())
                temp=get_rule(B,C)

                # print(temp)
                for l in range(len(temp)):
                    s1=temp[l][0]
                    r1=temp[l][1]
                    r2=temp[l][2]
                    prob_v=float(temp[l][-1])
                    if s1 in list(res[j][i].keys()):
                        if res[j][i][s1]<prob_v*float(res[j][k-1][r1])*float(res[k][i][r2]):
                            res[j][i][s1] = prob_v * float(res[j][k - 1][r1]) * float(res[k][i][r2])

                    else:

                        res[j][i][s1]=prob_v*float(res[j][k-1][r1])*float(res[k][i][r2])




                # B.extend(res[j][k - 1])
                # C.extend(res[k][i])




    print("PARSING SENTENCE:",s)
    n_pprase=list(res[0][n_words-1].keys()).count('S')
    print("NUMBER OF PARSES FOUND: ",n_pprase)
    print("TABLE:")
    for i in range(n_words):
        for j in range(n_words):
            if i<=j:
                print("cell[%d,%d]: "%(i+1,j+1),end="")
                if res[i][j]!={}:
                    for key,value in sorted(res[i][j].items()):
                        print("%s(%.4f) "%(key,value),end=" ")
                else:
                    print('-',end="")
                print()



if len(sys.argv)==3 or len(sys.argv)==5:
    for f in f2:
        cky(' '.join(f.split()))
        print()
        
elif len(sys.argv)==4 or len(sys.argv)==6:
    for f in f2:
        pcky(' '.join(f.split()))
        print()
    






