#coding:utf8
"""
Parse Stopwords List
Purpose: Add additional stopwords that names after `stopwords_<langageu>.txt`, 
    besides encoded with 'utf8'
date: 2021/1/15
"""
from os import path
import glob

from ..langcodes import LANGUAGE_CODE_BY_NAME

# appendix stopwords list
_fields = []
words = {}

def __get_words(filename):
    """Extract Words In File"""
    data = []
    with open(filename, encoding="utf8", mode="r") as file:
        for word in file.readlines():
            word = word.strip()
            if word:
                data.append(word)
    return data
    
def fields():
    """Add Method To Get Fields"""
    global _fields
    return _fields


for file in glob.glob(path.join(path.dirname(__file__), "*.txt")):
    name = path.splitext(path.basename(file))[0]
    field = name.split("_")[1] 
    
    if field in LANGUAGE_CODE_BY_NAME.values():
        _fields.append(field)
        words[field] = __get_words(filename=file)



del path, glob, __get_words