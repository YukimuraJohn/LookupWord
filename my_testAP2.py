""" An Application to find a word in a text """

import sys

def lookupWord(text, target):
    """ Search target into text and return a list of positions where it occurs """ 
    textList = text.split()
    return [i for i, x in enumerate(textList) if x == target]

def buildingIndex(text) -> dict[str, list[int]]:
    """ Buiding an inverted index"""
    textList = text.split()
    dic = {}
    for word in textList:
        dic[word] = lookupWord(text, word)
    return dic

def lookupWordFaster(target: str, index: dict) -> list[int]:
    """ Seaching using an inverted index """
    return index[target] if target in index else []

class LookUpWordClass():
    """ constructor from a string """
    def __init__(self, phrase):
        self._phrase = phrase
        self._index = buildingIndex(phrase)

    def getPositions(self, target) -> list[int]:
        """ Returns a list of positions where target occurs """
        return lookupWord(self._phrase, target)

    def getPositionFaster(self, target) -> list[int]:
        """ Returns a list of positions where target occurs, by using an inverted list"""
        return lookupWordFaster(target, self._index)

def main():

    phrase = "we dont need no education we dont need no thought control no we dont"
    print(f"phrase: '{phrase}'")

    target = str(input('Choose a Word: '))
    
    index = buildingIndex(phrase)
    print(f"inverted index: {index}")
    
    print(f"'{target}' -> lookupWord: {lookupWord(phrase, target)}")
    print(f"'{target}' -> lookupWordFaster: {lookupWordFaster(target, index)}")

    looker = LookUpWordClass(phrase)

    print(f"'{target}' -> getPositions: {looker.getPositions(target)}")

    print(f"'{target}' -> getPositionsFaster: {looker.getPositionFaster(target)}")

if __name__ == "__main__":
    sys.exit(main())