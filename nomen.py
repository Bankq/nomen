# -*- coding: utf-8 -*-
from xpinyin import Pinyin

from data import Data

p = Pinyin()
data = Data()
data.info()

print data.find("Jack"), p.get_pinyin(u"杰克", ' ')
print data.find("Mary"), p.get_pinyin(u"玛丽", ' ')
print data.find("Witham")
print data.find("Lagrange")

