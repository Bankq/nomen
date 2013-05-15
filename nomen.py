# -*- coding: utf-8 -*-
from data import *
from hyphen import Hyphenator, dict_info

class Nomen:
    
    def __init__(self):
        self.hyphen = Hyphenator('en_US')
        pass
    
    def load(self, file="./data/data-1.txt"):
        """ load training data"""
        self.data = Data()
        if self.data:
            print "Data loaded success"
            print str(self.data)

    def train(self):
        pass

    def rank(self):
        pass

    def get(self, en_name):
        en_name = en_name.lower()
        # lookup = self.data.find(en_name)
        # if lookup:
        #     return lookup

        syll = self.hyphen.syllables(en_name)
        split_onsets(syll)
        split_codas(syll)
        split_glides(syll)
        split_mcs(syll)
        expand_dipththongs(syll)
        print "Syllables:", syll
        return self.backward_max_matching(0, syll)

    def backward_max_matching(self, i, syll):
        if i >= (len(syll)):
            return ''
        if not syll or len(syll) == 0:
            return ''
        lx = self.data.lexicons
        key = ''.join(syll[i:])
        print "try:", key
        if key in lx:
            candidate = self.rank(lx[key], 0)
            print "find:", key, candidate
            return self.backward_max_matching(0,syll[0:i]) + self.rank(lx[key], 0)
        else:
            return self.backward_max_matching(i+1, syll)

    def rank(self, l, i):
        rl = sorted(l, reverse=True, key=lambda x:x[1])
        return rl[i][0]

if __name__ == "__main__":
    n = Nomen();
    n.load();
    n.train();


