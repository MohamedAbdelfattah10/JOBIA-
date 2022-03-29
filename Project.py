import spacy 
import re


    
 
def Clean(textt):
      txt.replace(',', ' ')
      txt.replace('/', ' ')
      txt.replace('\n', ' ')
      txt.replace('\\n', ' ')
      return txt



from collections import Counter 
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
 
# Driver program



def Skills(text):
    
    
    nlp=spacy.load("E:/Abdelfattah/NO Skills LG/model-last")
    skills=nlp(text)
    lis=[]
    for lem in skills.ents:
        lis.append(lem.text)

    return lis



def Jop_Titles_And_Companies(text):
    
    
    nlp=spacy.load("E:/Abdelfattah/Campanies_And_JobTitle LG After Update/model-best")
    jc=nlp(text)
    lis2=[]
    for lem in jc.ents:
        lis2.append(lem.text)

    return lis2


#print("SKILL:",Skills)
def Experience(text):
    nlp=spacy.load("E:/Abdelfattah/EX_LG/model-last")
    Experience=nlp(text)
    lis1=[]
    for lem in Experience.ents:
          lis1.append(lem.text)


    return lis1




def Phone_Numbers(text):
    nlp=spacy.load("en_core_web_lg")
    mydoc=nlp(text)
    phoneNumRegex = re.compile(r'[\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9]')
    mo = phoneNumRegex.findall(str(mydoc))
    return mo




def extract_emails(text):
    EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
    return re.findall(EMAIL_REG, text)
 

    

        

# Python program to demonstrate
# writing to CSV
  
# Python program to convert a list
# to string using join() function
    
# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))
        
        
# Driver code     

import csv 

def Database():      

    import numpy as np
      
      
    # data rows of csv file 
    rows = ["Skills",s] 
      
    # using the savetxt 
    # from the numpy module
    np.savetxt("GFG.csv", 
                rows,
                delimiter =", ", 
                fmt ='% s')




    
    
der="E:/Abdelfattah/First_Test_NER/Resumes Numbers/"
import os

list = os.listdir(der) # dir is your directory path
number_files = len(list)-1

index=0

for i in range(number_files):
    

    f = open('E:/Abdelfattah/First_Test_NER/Resumes Numbers/newfile' + str(index), 'r',encoding="utf-8")
    
    txt =str(f.read())
    #txt =str(f.readlines())
    txt=txt.rstrip("\n")
    print("CV"+str(index))
    print(txt)
    
    index=index+1
    
    inputt =txt
    s=remov_duplicates(inputt)
    
    jc=Jop_Titles_And_Companies(str(txt))
    print("Jop_Titles_And_Companies:",str(jc))
    
    
    Skillss=Skills(str(s))
    inputt =str(Skillss)
    
    s=remov_duplicates(inputt)
    print("SKILL:",str(s))
    
    Experiencee=Experience(str(txt))
    print("Experience:",Experiencee)
    
    phone_Numberss=Phone_Numbers(str(txt))
    print("PHONE_NUMBER:",phone_Numberss)
    
    emailss = extract_emails(txt)

    print("Email:",emailss) 
    Database()