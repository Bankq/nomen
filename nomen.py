# -*- coding: utf-8 -*-
from xpinyin import Pinyin

from data import Data

class Nomen:
    
    def __init__(self):
        pass
    
    def load(self, file="./data/data-1.txt"):
        """ load training data"""
        self.data = Data()
        if self.data:
            print "Data loaded success"
            print str(self.data)

    def train(self):
        """ Train the model """
        for ch, en in zip(self.data.ch, self.data.en):
            print ch, self.data.pinyin[ch], en, self.data.syllables[en]

    def rank(self):
        pass

    def get(self, en_name):
        """ Get the tranlisterate Chinesse name of input """
        pass


if __name__ == "__main__":
    n = Nomen();
    n.load();
    n.train();


