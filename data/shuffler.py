import random

with open('sentences.txt') as f:
    contents = f.read()

with open('randomized.txt', 'w') as f:
    contents = list(contents)
    random.shuffle(contents)
    print(''.join(contents), file=f)
