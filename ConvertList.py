import os
from .Word import Word
from .SentencePair import SentencePair

class ConvertList:
  @classmethod
  def build(self, inputFile, dictionary, sentences):
    dirname = os.path.dirname(__file__)
    convertedFile = os.path.join(dirname, './output.txt')
    f = open(inputFile, encoding='utf-8', errors='ignore')
    lines = f.readlines()
    
    converted = []
    for line in lines:
      item = line.strip()
      word = next((word for word in dictionary if word.kanji == item), '')
      if not word:
        continue
      sentence = next((pair.original() for pair in sentences if pair.ismatch(item)), '')
      translation = next((pair.translation() for pair in sentences if pair.ismatch(item)), '')
      string = item + "," + word.reading + "," + word.english + "," + sentence + "," + translation
      converted.append(string)

    with open(convertedFile, 'w', encoding='utf-8', errors='ignore') as f:
        for item in converted:
            f.write("%s\n" % item)

