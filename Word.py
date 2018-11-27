class Word:
  def __init__(self, kanji, reading, english):
    self.kanji = kanji
    self.reading = reading
    self.english = english.replace(",", " |")
