# Verification of Zipf's Law for Natural and Artificial Languages

## Introduction

Zipf’s Law is an empirical law that provides that in a given corpus, the rank of a word is inversely proportional to its frequency in the corpus; $rank \propto \frac{1}{frequency}$ 

We try to verify the validity of Zipf's Law first on a Natural Language, using a monolingual text corpus of Bahasa Indonesia. We then generate an Artificial Language and translate our monolingual corpus to form a new corpus in the Artificial Language, following which we repeat the verification of Zipf's Law.  

## User-Defined Modules 

* `cleaner.py` - Cleans the sentences of the corpus; `ind_wikipedia_2021_10K-sentences.txt` and stores it in `data/sentences.txt`
* `data/bahasa.py` - Plots relationship between rank and frequency in the original Indonesian corpus.
* `data/translationA.py` - Plots relationship between rank and frequency in the corpus translated with a simple Caesar Cipher.
* `data/translationB.py` - Plots relationship between rank and frequency in the corpus translated with a Caesar Cipher that includes blankspace character.
* `data/translationC.py` - Plots relationship between rank and frequency in the corpus translated with a Vigenere Cipher.
* `data/translationD.py` - Plots relationship between rank and frequency in the corpus translated with a Vigenere Cipher that includes blankspace character.
* `data/randomized.py` - Plots relationship between rank and frequency in the randomly shuffled corpus.
* `data/shuffler.py` - Shuffles the original Indonesian corpus and writes the resulting output to `data/randomized.txt`.
* `data/translator.py` - Defines a class for the Caesar Cipher.
* `data/vigenere.py` - Defines a class for the Vigenere Cipher.

## Directory Structure

```
.
├── cleaner.py
├── data
│   ├── bahasa
│   │   ├── bahasa_graph.png
│   │   ├── char_freq.png
│   │   ├── char_logfreq.png
│   │   ├── correlation_characters.txt
│   │   ├── correlation_words.txt
│   │   ├── words_freq.png
│   │   └── words_logfreq.png
│   ├── bahasa.py
│   ├── characters_randomized.txt
│   ├── characters_translationA.txt
│   ├── characters_translationB.txt
│   ├── characters_translationC.txt
│   ├── characters_translationD.txt
│   ├── characters.txt
│   ├── __pycache__
│   │   ├── translator.cpython-310.pyc
│   │   ├── translator.cpython-39.pyc
│   │   ├── vigenere.cpython-310.pyc
│   │   └── vigenere.cpython-39.pyc
│   ├── randomized
│   │   ├── char_freq.png
│   │   ├── char_logfreq.png
│   │   ├── correlation_characters.txt
│   │   ├── correlation_words.txt
│   │   ├── randomized.png
│   │   ├── words_freq.png
│   │   └── words_logfreq.png
│   ├── randomized.py
│   ├── randomized.txt
│   ├── sentences_translationA.txt
│   ├── sentences_translationB.txt
│   ├── sentences_translationC.txt
│   ├── sentences_translationD.txt
│   ├── sentences.txt
│   ├── shuffler.py
│   ├── tokens_randomized.txt
│   ├── tokens_translationA.txt
│   ├── tokens_translationB.txt
│   ├── tokens_translationC.txt
│   ├── tokens_translationD.txt
│   ├── tokens.txt
│   ├── translationA
│   │   ├── char_freq.png
│   │   ├── char_logfreq.png
│   │   ├── correlation_characters.txt
│   │   ├── correlation_words.txt
│   │   ├── translationA_graph.png
│   │   ├── words_freq.png
│   │   └── words_logfreq.png
│   ├── translationA.py
│   ├── translationB
│   │   ├── char_freq.png
│   │   ├── char_logfreq.png
│   │   ├── correlation_characters.txt
│   │   ├── correlation_words.txt
│   │   ├── translationB_graph.png
│   │   ├── words_freq.png
│   │   └── words_logfreq.png
│   ├── translationB.py
│   ├── translationC
│   │   ├── char_freq.png
│   │   ├── char_logfreq.png
│   │   ├── correlation_characters.txt
│   │   ├── correlation_words.txt
│   │   ├── translationC_graph.png
│   │   ├── words_freq.png
│   │   └── words_logfreq.png
│   ├── translationC.py
│   ├── translationD
│   │   ├── char_freq.png
│   │   ├── char_logfreq.png
│   │   ├── correlation_characters.txt
│   │   ├── correlation_words.txt
│   │   ├── translationD_graph.png
│   │   ├── words_freq.png
│   │   └── words_logfreq.png
│   ├── translationD.py
│   ├── translator.py
│   └── vigenere.py
├── ind_wikipedia_2021_10K-co_n.txt
├── ind_wikipedia_2021_10K-co_s.txt
├── ind_wikipedia_2021_10K-import.sql
├── ind_wikipedia_2021_10K-inv_so.txt
├── ind_wikipedia_2021_10K-inv_w.txt
├── ind_wikipedia_2021_10K-sentences.txt
├── ind_wikipedia_2021_10K-sources.txt
├── ind_wikipedia_2021_10K-words.txt
├── README.md
└── requirements.txt

8 directories, 84 files
```