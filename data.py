# -*- coding: utf-8 -*-

import codecs

class Data:
    "Parse file into class Data"
    def __init__(self, filepath="./data/data-1.txt"):
        self.filepath = filepath
        self.ch = []
        self.en = []
        self.count = 0
        self.parse()
    
    def parse(self):
        with codecs.open(self.filepath, encoding='utf-8', mode='r') as f:
            for line in f:
                self.count = self.count + 1
                line = line[0:-1]
                words = line.split()
                if len(words) != 2:
                    print "Error on line", self.count
                    raise ValueError
                self.ch.append(words[0])
                self.en.append(words[1])
    
    def info(self):
        print "File:",self.filepath
        print self.count, "name pairs"

    def find(self, key):
        try:
            return self.en[self.ch.index(key)]
        except ValueError:
            try:
                return self.ch[self.en.index(key)]
            except ValueError:
                return None
