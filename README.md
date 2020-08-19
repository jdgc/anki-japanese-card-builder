# Anki Japanese Card Builder
Anki 2.1 addon that generates and populates JP > EN flashcards from a .txt list

## Setup

Add to addons21 folder in Anki directory

## How To Use

Open Anki and select the option 'Generate from list (日本語)' From the tools menu.
Select an input file to begin card generation according to the specified configuration (see Config)

## Input file

The input file should be a .txt file with a single Japanese word on each line.

eg:

``` txt
迷彩
仮眠
自白
祖国
こそこそ
雨乞い
映える
企業買収
プッツン
土葬
秘匿
公爵
```
Verbs should be listed in 'dictionary' or 'plain' form. 

## Output

When importing the list of words, cards will be built including their reading (in hiragana), english translation, and an example sentence including the word if available (including the english translation of this sentence)

## Config

Select Deck name and Note type (card template) from the config option of the addons menu in the Anki main application prior to importing for the first time.

## Data Source

Dictionary lookup is performed with the [JMdict/EDICT](http://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) dictionary.  
Sentences are sourced from the Tatoeba project hosted at [tatoeba.org](https://tatoeba.org)


