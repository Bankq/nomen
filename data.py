# -*- coding: utf-8 -*-

import codecs
from hyphen import Hyphenator, dict_info
from xpinyin import Pinyin

sound_non_vowels = ['b', 'c', 'd', 'f', 'g', 'k', 'm', 'p', 'q', 's', 't', 'z']
glides = ['l', 'r', 'w']
vowels = ['a', 'o', 'e', 'i', 'u']
onsets = ['st', 'sk']


class Data(object):
    """Parse file into class Data"""
    def __init__(self, filepath="./data/data-1.txt"):

        self.filepath = filepath
        self.ch = []
        self.en = []
        self.syllables = []
        self.pairs = []
        self.lexicon = {}
        self.pinyin = []
        self.count = 0
        self.parse()
        self.align()
        self.produce_lexicon()

    def __repr__(self):
        return "File: "+self.filepath+" . Contains "+str(self.count)+" name pairs."

    def __str(self):
        return "File: "+self.filepath+" . Contains "+str(self.count)+" name pairs."
    
    def parse(self):
        p = Pinyin()
        s = Hyphenator('en_US')
        with codecs.open(self.filepath, encoding='utf-8', mode='r') as f:
            for line in f:
                self.count = self.count + 1
                line = line[0:-1]
                words = line.split()
                if len(words) != 2:
                    print "Error on line", self.count
                    raise ValueError
                c = words[0].strip()
                e = words[1].strip().lower()

                self.ch.append(c)
                self.pinyin.append(p.get_pinyin(c, ' ').split())

                self.en.append(e)
                if len(e) > 3:
                    syll= s.syllables(e)
                    syll = self.sub_syllables(e, c, syll)
                else:
                    syll = [e]
                self.syllables.append(syll)
                
    def sub_syllables(self, e, c, syllables):
        """ Continue split syllables based on corresponding Chinese """
        split_onsets(syllables)
        split_codas(syllables)
        if u'尔' in c or u'夫' in c:
            split_glides(syllables)
        if u'麦' in c:
            split_mcs(syllables)
        expand_dipththongs(syllables)
        return syllables


    def align(self):
        """ align one/multiple Chinese character(s) with one/multiple syllables"""
        for i in range(self.count):
            c = self.ch[i]
            syll = self.syllables[i]
            self.pairs.append(do_align(c, syll))



    def produce_lexicon(self):
        for i in self.pairs:
            # i is a list of tuples (ch, syll)
            
            pass
        pass
        
    def find(self, key):
        try:
            return self.en[self.ch.index(key)].title()
        except ValueError:
            try:
                key = key.lower()
                return self.ch[self.en.index(key)]
            except ValueError:
                return None

    def index(self, value):
        try:
            return self.en.index(value.lower())
        except ValueError:
            try:
                return self.ch.index(value)
            except ValueError:
                return None

def do_align(c, syll):
    l = []
    while True:
        if len(c) == 0 or len(syll) == 0:
            break
        
        if len(c) == 3 and len(syll) == 1:
            ci = c
            c = ''
            ei = syll[0]
            syll = ''

        elif len(c) <= len(syll):                    

            if len(c) == 1:
                ci = c[0]
                c = c[1:]
                #last Chinese char with more syllables left
                #combine all left syllables
                ei = ''.join(syll)
                syll = ''
            else:
                ci = c[0]
                c = c[1:]
                ei = syll[0]
                syll = syll[1:]
        else:
            if len(syll) == 1:
                ei = syll[0]
                syll = ''
                ci = c
                c = ''
            elif len(syll[0]) > 3:
                ei = syll[0]
                ci = c[0:2]
                syll = syll[1:]
                c = c[2:]
            else:
                ci = c[0]
                c = c[1:]
                ei = syll[0]
                syll = syll[1:]
            
        t = ci, ei
        l.append(t)    
    return l

def split_onsets(syllables):
    for o in onsets:
        for i, s in enumerate(syllables):
            try:
                p = s.index(o)
                s1 = s[:p]
                s2 = s[p:p+1]
                s3 = s[p+1:]
                syllables.remove(s)
                if len(s3) > 0:
                    syllables.insert(i, s3) 
                if len(s2) > 0:
                    syllables.insert(i, s2)
                if len(s1) > 0:
                    syllables.insert(i, s1) 
            except ValueError:
                pass
    return syllables


def split_codas(syllables):
    for i, s in enumerate(syllables):
        if len(s) > 1 and s[-2] in vowels and s[-1] in sound_non_vowels:
            s1 = s[:-1]
            s2 = s[-1:]
            syllables.remove(s)
            if len(s2) > 0:
                syllables.insert(i, s2)
            if len(s1) > 0:
                syllables.insert(i, s1)
    return syllables


def split_glides(syllables):
    for i, s in enumerate(syllables):
        if len(s) > 1 and s[-2] in vowels and s[-1] in glides:
            s1 = s[:-1]
            s2 = s[-1:]
            syllables.remove(s)
            if len(s2) > 0:
                syllables.insert(i, s2)
            if len(s1) > 0:
                syllables.insert(i, s1)
    return syllables

def expand_dipththongs(syllables):
    for i, s in enumerate(syllables):
        if len(s) > 1 and 'ia' in s:
            try:
                p = s.index('ia')
                s1 = s[:p]
                s2 = 'i'
                s3 = 'a'
                syllables.remove(s)
                syllables.insert(i, s3)
                syllables.insert(i, s2)
                if len(s1) > 0:
                    syllables.insert(i, s1)
            except ValueError:
                pass
    return syllables

def split_mcs(syllables):
    for i, s in enumerate(syllables):
        if len(s) > 1 and s[0] == 'm' and s[1] == 'c':
            s1 = 'm'
            s2 = 'c'
            s3 = s[2:]
            syllables.remove(s)
            if len(s3) > 0:
                syllables.insert(i, s3)
            syllables.insert(i, s2)
            syllables.insert(i, s1)
    return syllables
