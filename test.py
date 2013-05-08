# -*- coding: utf-8 -*-

from .data import Data
data = Data()

def test_file():
    assert data.count == 17613 and len(data.ch) == len(data.en)

def test_find():
    assert data.find(u"西奥") == "Theo"
    assert data.find("Theo") == u"西奥"
    assert data.find("ChuckNorris") is None
