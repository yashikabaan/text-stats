from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from matplotlib import pyplot as plt

class App(Tk):
    def __init__(self):
        super().__init__()
        self.filePath = ""
        self.cachedFile = ""
        self.keywordFilePath = ""
        self.numWords = 0
        self.numSentences = 0
        self.newLines = 0
        self.mostFrequentWords = []
        self.leastFrequentWords = []
        self.sentencesWithKeywords = []
        
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
        Plot button code
        """

        """
        Sentences with Keyword Frame/Section code
        """

    def updateFilePath(self):
        """
        TODO : add docstring
        """
        self.filePath = filedialog.askopenfilename()  # Updates field
        self.filePathLabel.config(text = "File: " + self.filePath) # Updates the GUI
        self.readFileAndUpdateStatistics()

    def readFileAndUpdateStatistics(self):
        """
        Reads File from filePath field.
        Updates the statistics fields.
        Calls updateStatistics to update GUI.
        Caches the file in the cachedFile field.
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
        TODO Add frequencies and cache
        """
        return
        

    def updateStatistics(self):
        """
        Updates the Statistics Frame/Section section's GUI
        using config method on each element.
        Uses helper functions to compute the statistics.
        @params : None
        @returns : None
        """
        self.readFileAndUpdateStatistics()
        return

    def updateKeyword(self):
        """
        Browses the keyword file using browseFile.
        Updates the field sentencesWithKeywords.
        Updates the GUI for Sentences with Keyword Frame/Section.
        @params : None
        @returns : None
        """
        raise NotImplementedError

    def plotHist(self):
        """
        Plots histogram.
        @params : None
        """
        raise NotADirectoryError
