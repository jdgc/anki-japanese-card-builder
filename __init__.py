import os
from .Dictionary import Dictionary
from .Sentences import Sentences
from .ConvertList import ConvertList
from .Word import Word
from .SentencePair import SentencePair
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from anki.importing import TextImporter

config = mw.addonManager.getConfig(__name__)

dirname = os.path.dirname(__file__)
importFile = os.path.join(dirname, './output.txt')

dictionary = Dictionary.setup()
sentences = Sentences.setup()

def generateFromList():
    fileName = QFileDialog.getOpenFileName(mw, "Select Text File", "/", "Text files (*.txt)")[0]
    
    # set 
    if fileName is None:
      showInfo("Please select a file." % fileName)
      return
    else:
      ConvertList.build(fileName, dictionary, sentences)

    # select target deck
    deckName = config["deckName"]
    did = mw.col.decks.id(deckName)
    mw.col.decks.select(did)
    m = mw.col.models.byName(config["noteType"])
    deck = mw.col.decks.get(did)
    deck['mid'] = m['id']
    mw.col.decks.save(deck)
    m['did'] = did
    
    # import cards into selected deck
    ti = TextImporter(mw.col, importFile)
    ti.initMapping()
    ti.run()
    mw.reset()
    showInfo("imported successfully!")

action = QPushButton("Generate from list", mw)
action.setMinimumSize(200, 20)
action.clicked.connect(generateFromList)