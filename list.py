from configparser import NoSectionError
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize #to tokenize our list
from nltk.corpus import stopwords     # to remove reoccuring stopwrods liek A, An, The ,etc
from nltk.stem.snowball import EnglishStemmer
    
from collections import defaultdict
# print(stopwords.words('english'))

class IndexTask:

    def __init__(self,exampleList) :
        self.exampleList=exampleList
        self.wordinlist=[]
        self.noStopWordList=[]
        self.stemmer=EnglishStemmer()
        self.inverted_index=defaultdict(set)
        
    # def parseList(self):
    #     stopWords=set(stopwords.words('english'))
    #     # print(stopWords) ## all small ma raicha

    #     for alist in self.exampleList:
    #         wordTokens=word_tokenize(alist)
    #         self.noStopWordList=self.noStopWordList+([w.lower() for w in wordTokens if not w.lower() in stopWords])
    #     self.noStopWordList=set(self.noStopWordList)  
    #     print((self.noStopWordList))
    #     self.wordinlist=list(self.noStopWordList)

    #     return True

    def createIndex(self):
        stopWords=set(stopwords.words('english'))
        
        for itsid, alist in enumerate(self.exampleList):
            for sent in sent_tokenize(alist):
                 for word in word_tokenize(sent):
                    # print(word)
                    if not word.lower() in stopWords:
                        word=word.lower()
                        self.inverted_index[word].add(itsid)
        print((self.inverted_index))


        return True
    def lookupSearch(self,searchField):
        searchField=searchField.lower()
       
        idmatched=self.inverted_index.get(searchField)
        print(idmatched)
        if idmatched:
            for id in idmatched:
                print(self.exampleList[id])
           
            



        # return True

exampleList=[
            'My name is Abhinav abhinav',
            'I am currently doing this taks',
            'Abhinav is doing a task',
            'We all love Nepal']

classObj=IndexTask(exampleList)

classObj.createIndex()
searchInputs=['love','abhinav']
for input in searchInputs:
    classObj.lookupSearch(input)
