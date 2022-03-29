import en_core_web_lg
import pandas as pd 
import re
import spacy
from collections import Counter 

nlp = spacy.load('en_use_md')

def remov_duplicates(input):
 
    # split input string separated by space
    input = input.split(" ")
 
    # joins two adjacent elements in iterable way
    for i in range(0, len(input)):
        input[i] = "".join(input[i])
 
    # create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    UniqW = Counter(input)
 
    # joins two adjacent elements in iterable way
    s = " ".join(UniqW.keys())
    return s

## try medium or large spacy english models
skills=pd.read_csv("E:/Abdelfattah/First_Test_NER/GFG.csv")
skills=skills['Skills']
skills=str(skills)

skills=re.sub("'", '', skills).replace("   "," ")
#skills=re.sub("'", '', skills).replace(" ",",")
skills=re.sub("'", '', skills).replace("["," ")
skills=re.sub("'", '', skills).replace("]"," ").lower()

data2=pd.read_csv("C:/Users/Mohamed Abdelfattah/OneDrive/Desktop/JOP/Jop_Skills.csv")

df=data2.loc[data2['job_title']== "moo"]['keyword_name'].tolist()
df=re.sub("'", '', str(df)).replace(" ","")
df=re.sub("'", '', str(df)).replace(","," ")
df=re.sub("'", '', str(df)).replace("["," ")
df=re.sub("'", '', str(df)).replace("]"," ").lower()
test=remov_duplicates(df)
doc1 = nlp(str(skills))
print(doc1)

print("-----------------")

doc2 = nlp(str(test))
print(doc2)


# cosine similarity
print(doc1.similarity(doc2)) 




