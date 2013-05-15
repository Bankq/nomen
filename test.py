# -*- coding: utf-8 -*-

from .data import *
from .nomen import Nomen
#from .syllabifier import loadLanguage, syllabify, stringify, English
from hyphen import Hyphenator, dict_info

data = Data()
h = Hyphenator('en_US')

def test_align():
    for l in data.pairs:
        for t in l:
            print t[0], t[1]

def test_lexicons():
    l = [(u'你', u'you'), (u'好', u'me'), (u'美', u'awesome')]
    lexi = {}
    generate_lexicons(l,lexi)
    assert len(lexi.keys()) == 6
    for i in data.lexicons['thing']:
        print i[0], i[1]

def test_file():
    assert data.count == 17613 and len(data.ch) == len(data.en)

def test_find():
    assert data.find(u"西奥") == "Theo"
    assert data.find("Theo") == u"西奥"
    print data.syllables[data.index(u'沃特')]
    for t in data.pairs[data.index(u'沃辛顿')]:
        print t[0], t[1]
    assert data.find("ChuckNorris") is None

def test_nomen():
    n = Nomen()
    n.load()
    print n.get(u'Disneyton')

def test_hyphenator():
    s = h.syllables(u"Wat")
    print s
    assert len(s) is 2

def test_split_onsets():
    s = h.syllables(u"stewart")
    print s
    ss = split_onsets(s)
    print ss
    assert len(ss) is 3


def test_split_codas():
    s = h.syllables(u"minkowski")
    print s
    ss = split_onsets(s)
    ss = split_codas(ss)
    print ss
    assert len(ss) is 3


def test_split_glides():
    s = h.syllables(u"minkowski")
    print s
    ss = split_onsets(s)
    ss = split_codas(ss)
    ss = split_glides(ss)
    print ss
    assert len(ss) is 4

def test_split_mcs():
    s = h.syllables(u'mcdonald')
    print s
    ss = split_mcs(s)
    print ss
    assert len(ss) is 4

def test_expand_dipththongs():
    s = h.syllables(u'amelia')
    print s
    ss = expand_dipththongs(s)
    print ss
    assert len(ss) is 3
