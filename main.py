import random
from typing import List

with open("Text2Convert.txt", "r") as f:
    text2Convert: str= f.read()

with open("Introductions.txt", "r") as f:
    introductions: List[str] = f.read().split("\n")

def convertSentence(s: str, firstInLine: bool) -> str:
    if len(s)==0:
        return s
    charAtBeginning = ""
    firstCharIndex = 0
    nonChars = set(" ")
    for i, c in enumerate(s):
        if c not in nonChars:
            firstCharIndex = i
            break
    #lower of first character in a sentence
    s = list(s)
    s[firstCharIndex] = s[firstCharIndex].lower()
    s = "".join(s)

    if s[0] != " " and not firstInLine:
        charAtBeginning = " "
    
    charBetween = " "
    if s[0] == " ":
        charBetween = ""

    return charAtBeginning + random.choice(introductions) + charBetween + s

lines2Convert = text2Convert.split("\n")

convertedSentences:List[str] = []
for i, line in enumerate(lines2Convert):
    sentences2Convert: List[str] = line.split(".")
    sentences2Convert = list(filter(lambda s: len(s)>0, sentences2Convert))

    for m, sentence in enumerate(sentences2Convert):
        if m == 0:
            convertedSentence: str = convertSentence(sentence, True)
        else:
            convertedSentence: str = convertSentence(sentence, False)
        convertedSentences.append(convertedSentence)
    convertedSentences += ["\n"]

text2Write: str = ""
for line in convertedSentences:
    print([line])
    text2Write += line
    if line != "\n":
        text2Write += "."

with open("ConvertedText.txt", "w") as f:
    f.write(text2Write)
