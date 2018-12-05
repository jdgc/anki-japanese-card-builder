class SentencePair:
  def __init__(self, list_tuple):
    self.A = list_tuple[0].partition("#")[0] \
                          .replace(",", "").strip("A: ")
    self.B = list_tuple[1].strip()

  def ismatch(self, word):
    return word in self.B

  def translation(self):
    return self.A.partition("\t")[-1]

  def original(self):
    return self.A.partition("\t")[0]