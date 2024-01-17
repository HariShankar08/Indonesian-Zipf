import os
import matplotlib.pyplot as plt
import math
import json
import warnings
import numpy as np

warnings.filterwarnings("ignore")


if not os.path.exists('tokens.txt'):
    os.system("tr -sc 'A-Za-z' '\n' < sentences.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr > tokens.txt")

if not os.path.exists('characters.txt'):
    os.system("tr '[:upper:]' '[:lower:]' < sentences.txt | tr -sc 'A-Za-z' '\n' | egrep -o '.' | sort | uniq -c | sort -nr > characters.txt")

with open('tokens.txt', 'r') as f:
    # rank = index of word in list + 1
    # (word, freq) == items of list
    ranked_words_freq = [l.strip().split() for l in f.readlines()]
    ranked_words_freq = [i for i in ranked_words_freq if len(i) == 2]
    ranked_words_freq = list(map(lambda x: (x[1], int(x[0])), ranked_words_freq))

freq = [w[1] for w in ranked_words_freq]
rank = list(range(1, len(freq)+1))

plt.plot(freq)
plt.savefig('bahasa/words_freq.png')
plt.show()

with open('bahasa/correlation_words.txt', 'w') as f:
    print(f"Correlation (words) rank, frequency: {np.corrcoef(freq, rank)[0][1]}", file=f)

logfreq = list(map(math.log10, freq))
logrank = list(map(math.log10, rank))
           
plt.figure()
plt.plot(logrank, logfreq, c='b')
plt.savefig('bahasa/words_logfreq.png')
plt.show()

with open('characters.txt', 'r') as f:
    # rank = index of word in list + 1
    # (word, freq) == items of list
    ranked_char_freq = [l.split() for l in f.readlines() if len(l.split()) == 2]
    ranked_char_freq = list(map(lambda x: (x[1], int(x[0])), ranked_char_freq))

freq = [w[1] for w in ranked_char_freq]
rank = list(range(1, len(freq)+1))

plt.plot(freq)
plt.savefig('bahasa/char_freq.png')
plt.show()

logfreq = list(map(math.log10, freq))
logrank = list(map(math.log10, rank))
               
plt.plot(logrank, logfreq)
plt.savefig('bahasa/char_logfreq.png')
plt.show()

with open('bahasa/correlation_characters.txt', 'w') as f:
    print(f"Correlation (characters) rank, frequency: {np.corrcoef(freq, rank)[0][1]}", file=f)
