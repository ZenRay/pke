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
_fields = [
    file.split("_")[1] for file in glob.glob(path.join(path.dirname(__file__), "*.txt"))
    if file.split("_")[1] in LANGUAGE_CODE_BY_NAME
]

def __get_words(filename):
    """Extract Words In File"""
    data = []
    with open(filename, encoding="utf8", mode="r") as file:
        for word in file.readlines():
            word = word.strip()
            if word:
                data.append(word)
    return data
    
words = {
    field: __get_words(
        path.join(path.dirname(__file__), f"stopwords_{field}")
    ) for field in _fields
}