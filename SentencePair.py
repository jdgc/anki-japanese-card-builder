class SentencePair:
  def __init__(self, list_tuple):
    self.A = list_tuple[0].partition("#")[0] \
                          .replace(",", "").strip()
    self.B = list_tuple[1].strip()

  def ismatch(self, word):
    return word in self.B