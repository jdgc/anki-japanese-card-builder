import os
import xml.etree.ElementTree as ET
from .Word import Word

class Dictionary:
   @classmethod
   def setup(self):
      dictionary = []
      dirname = os.path.dirname(__file__)
      filename = os.path.join(dirname, './JMdict_e.xml')
      tree = ET.parse(filename)
      root = tree.getroot()
      for entry in root.findall("./entry"):
        kanji = entry.find('./k_ele')
        if kanji == None:
          kanji = entry.find('./r_ele')[0].text
        else:
          kanji = kanji[0].text
        reading = entry.find('./r_ele')[0].text
        english = ""
        for index, gloss in enumerate(entry.findall('./sense/gloss')):
          if index != 0: 
            english += ", "
          english += gloss.text
        word = Word(kanji, reading, english)
        dictionary.append(word)
      return dictionary     
