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

        """
        Keyword File Browse Button code
        """
        
        """
        Statistics Frame/Section
        """

        """
        Plot button code
        """

        """
        Sentences with Keyword Frame/Section code
        """

    def browseFile(self):
        """
        TODO : add docstring
        """
        return filedialog.askopenfilename() # TODO : Add file exists check

    def updateFilePath(self):
        """
        TODO : add docstring
        """
        self.filePath = browseFile() # Updates field
        self.filePathLabel.config(text = "File: " + self.filePath) # Updates the GUI
        readFileAndUpdateStatistics()

    def readFileAndUpdateStatistics(self):
        """
        Reads File from filePath field.
        Updates the statistics fields.
        Calls updateStatistics to update GUI.
        Caches the file in the cachedFile field.
        @params : None
        @returns : None 
        """
        raise NotImplementedError

    def updateStatistics(self):
        """
        Updates the Statistics Frame/Section section's GUI
        using config method on each element.
        Uses helper functions to compute the statistics.
        @params : None
        @returns : None
        """
        raise NotImplementedError

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
