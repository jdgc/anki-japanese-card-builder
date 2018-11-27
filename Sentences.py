import os
from .SentencePair import SentencePair

class Sentences:
  @classmethod
  def setup(self):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, './examples.txt')
    f = open(filepath, encoding='utf-8', errors='ignore')
    lines = f.readlines()
    zipped = zip(lines[0::2], lines[1::2])
    grouped = list(zipped)
    pairs = []
    for pair in grouped:
      pairs.append(SentencePair(pair))
    return pairs