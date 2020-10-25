from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from typing import Counter
from matplotlib import pyplot as plt
import numpy as np
from statistics import mode
from nltk.corpus import stopwords
import re

class App(Tk):
    def __init__(self):
        super().__init__()
        self.filePath = ""
        self.keywordFilePath = ""
        self.numWords = 0
        self.numSentences = 0
        self.newLines = 0
        self.words = []
        self.mostFrequentWords = ""
        self.leastFrequentWords = ""
        self.sentencesWithKeywords = ""
        self.sentences = []
        self.commonwords = set(stopwords.words('english'))
        
        """
        All initializations are below
        """
        self.geometry('500x500')
        self.grid()
        
        """
        File Path Label code
        """
        self.filePathLabel = Label(self, text = "File: " + self.filePath)
        self.filePathLabel.pack()
        self.keywordFilePathLabel = Label(self, text = "Keywords File: " + self.keywordFilePath)
        self.keywordFilePathLabel.pack()
        
        """
        Browse Button code
        """
        self.browseButton = ttk.Button(self, text = "Browse", command = self.updateFilePath)
        self.browseButton.pack()

        """
        Refresh Button code : calls readFileAndUpdateStatistics
        """
        self.refreshButton = ttk.Button(self, text="Refresh", command=self.readFileAndUpdateStatistics)
        self.refreshButton.pack()

        """
        Keyword File Browse Button code
        """
        self.browseKeywordButton = ttk.Button(self, text = "Browse Keyword File", command = self.updateKeywordFilePath)
        self.browseKeywordButton.pack()

        """
        Statistics Frame/Section
        """
        self.numWordsLabel = Label(self, text="Words: " + str(self.numWords))
        self.numWordsLabel.pack()
        self.numSentencesLabel = Label(self, text="Sentences: " + str(self.numSentences))
        self.numSentencesLabel.pack()
        self.newLinesLabel = Label(self, text="Lines: " + str(self.newLines))
        self.newLinesLabel.pack()

        """
        Labels for frequencies
        """
        self.mostFrequentWordsLabel = Label(self, text="Most Frequent Word: " + (self.mostFrequentWords))
        self.mostFrequentWordsLabel.pack()
        self.leastFrequentWordsLabel = Label(self, text="Least Frequent Word: " + (self.leastFrequentWords))
        self.leastFrequentWordsLabel.pack()

        """
        Plot button code
        """
        self.plotButton = ttk.Button(self, text="Plot Histogram", command=self.plotHist)
        self.plotButton.pack()

        """
        Sentences with Keyword Frame/Section code
        """
        self.sentencesWithKeywordsLabel = Label(self, text="Sentences with Keywords: " + str(self.sentencesWithKeywords))
        self.sentencesWithKeywordsLabel.pack()

    def updateFilePath(self):
        """
        TODO : add docstring
        """
        self.filePath = filedialog.askopenfilename()  # Updates field
        self.filePathLabel.config(text = "File: " + self.filePath) # Updates the GUI
        self.readFileAndUpdateStatistics()

    def updateKeywordFilePath(self):
        """
        TODO : add docstring
        """
        self.keywordFilePath = filedialog.askopenfilename()  # Updates field
        self.keywordFilePathLabel.config(text = "Keywords File: " + self.keywordFilePath) # Updates the GUI
        self.updateKeyword()
        

    def readFileAndUpdateStatistics(self):
        """
        Reads File from filePath field.
        Updates the statistics fields and GUI.
        Caches the file in the words and sentences.
        @params : None
        @returns : None 
        """
        file = open(self.filePath,"rt")
        text = file.read()
        self.numWords = len(text.split())
        self.numWordsLabel.config(text="Words: " + str(self.numWords))

        self.numSentences = text.count('.') + text.count('?') + text.count('!')
        self.numSentencesLabel.config(text="Sentences: " + str(self.numSentences))

        self.newLines = text.count('\n')
        self.newLinesLabel.config(text="Lines: " + str(self.newLines))

        """
        Frequencies 
        """
        self.words = text.split()
        wordFrequency = Counter(self.words)
        highest = wordFrequency[mode(self.words)]
        lowest = wordFrequency[wordFrequency.most_common()[-1][0]]
        self.mostFrequentWords = "  "
        self.leastFrequentWords = "  "
        enum=0
        for word in wordFrequency:
            if word not in commonwords:
                if(enum > 5):
                    self.mostFrequentWords+="..."
                    break
                elif wordFrequency[word] == highest:
                    self.mostFrequentWords+=word+", "
                    enum+=1

        enum=0
        for word in wordFrequency:
            if word not in commonwords:
                if enum>5:
                    self.leastFrequentWords+="..."
                    break
                elif wordFrequency[word] == lowest:
                    self.leastFrequentWords+=word+ ", "
                    enum+=1
        self.mostFrequentWordsLabel.config(text="Most Frequent Word(s): " + str(self.mostFrequentWords))
        self.leastFrequentWordsLabel.config(text="Least Frequent Word(s): " + str(self.leastFrequentWords))
        self.sentences = []
        with open(self.filePath) as file:
            for line in file:
                for l in re.split(r"(\. |\? |\! )",line):
                    self.sentences.append(l)
        self.updateKeyWord();
        

    def updateKeyword(self):
        """
        Browses the keyword file using browseFile.
        Updates the field sentencesWithKeywords.
        Updates the GUI for Sentences with Keyword Frame/Section.
        @params : None
        @returns : None
        """
        file = open(self.keywordFilePath, "rt")
        text = file.read()
        search_keywords = text.split()
        self.sentencesWithKeywords = ""
        for sentence in self.sentences:
            s = sentence.split(" ")
            for word in search_keywords: 
                for i in s:
                    if word == i and not(sentence in self.sentencesWithKeywords):
                        # print(word, sentence)
                        self.sentencesWithKeywords += (sentence)
                        self.sentencesWithKeywords += ("\n")
        self.sentencesWithKeywordsLabel.config(text="Sentences with keywords: " + "\n" + (self.sentencesWithKeywords))

    def plotHist(self):
        """
        Plots histogram.
        @params : None
        """        
        labels,counts = np.unique(self.words,return_counts=True)
        ticks = range(len(counts))
        plt.bar(ticks,counts,align='center')
        plt.xticks(ticks,labels)
        plt.show()
