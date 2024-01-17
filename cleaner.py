with open('ind_wikipedia_2021_10K-sentences.txt') as f:
    l = []
    for line in f.readlines():
        l.append(line.split(' ', maxsplit=1)[1].strip())


with open('data/sentences.txt', 'w') as f:
    print('\n'.join(l), file=f)
