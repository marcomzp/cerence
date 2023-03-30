import re
import math 
import numpy as np
from collections import Counter
# -*- coding: <utf-8> -*-

#The function below calculates bigrams for the trainig data after doing some text processing.  
def bigrams_training(x):
    a = open(x).read()
    b = a.replace("\'", "") 
    c= b.lower() #making everything lower case
    words = re.findall('\w+|\.|\?', c)
    bigrams = Counter(zip(words,words[1:]))
    return bigrams  

    #The function below calculates unigrams for the training data after doing some text processing.  
def unigrams_training(x):
    a = open(x).read()
    b = a.replace("\'", "") 
    c= b.lower() #making everything lower case
    words = re.findall('\w+|\.|\?', c)
    unigrams = Counter(zip(words))
    return unigrams

#The function below calculates the MLE for the training data.  
def probs_training(bigrams, unigrams):
    d = {}
    for k_b, v_b in bigrams.items():
        for  k_u, v_u in unigrams.items():
            if k_b[0] in k_u:
                prob = v_b/v_u
                d[k_b] = prob
                #print(prob)
    return d


#the function below calculates bigrams for the test data after doing some text processing.
def bigrams_test():
    test_bi = []
    with open('LangId.test') as f:
        #content = f.readlines()
        for line in f:
            line = line.lower()
            w = re.findall('\w+|\.|\?', line)
            bigrams = Counter(zip(w,w[1:]))
            test_bi.append(list(bigrams.keys()))
    return test_bi    



#The variables below assign different probability models for each language/ 
eng_bigrams = bigrams_training('LangId.train.English')
#print(eng_bigrams)
eng_unigrams = unigrams_training('LangId.train.English')
probs_eng = probs_training(eng_bigrams, eng_unigrams)


fr_bigrams = bigrams_training('LangId.train.French')
fr_unigrams = unigrams_training('LangId.train.French')
probs_fr = probs_training(fr_bigrams, fr_unigrams)

it_bigrams = bigrams_training('LangId.train.Italian')
it_unigrams = unigrams_training('LangId.train.Italian')
probs_it = probs_training(it_bigrams, it_unigrams)
#print(probs_it)

test_bigrams = bigrams_test()  
#print(test_bigrams)


#The code below gives me how many times I got the language correctly.
with open('LangId.sol', 'r') as myfile:
    data=myfile.read()
for i in data:
     w = re.findall('\w+', data)
no_integers = [x for x in w if not (x.isdigit() 
                                         or x[0] == '-' and x[1:].isdigit())]
import itertools


print(len([i for i, j in zip(result, no_integers) if i == j]))

