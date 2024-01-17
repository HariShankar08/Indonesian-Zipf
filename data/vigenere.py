import random


class Vigenere:
    def __init__(self, characters, key):
        self.characters = characters
        self.key = key

        self.translator_square = {}
        for i, al in enumerate(self.characters):
            dict_thing = {}
            for j, alp in enumerate(self.characters):
                dict_thing[alp] = self.characters[(i+j) % len(self.characters)]
            self.translator_square[al] = dict_thing
        
    
    def transform(self, text):
        text = text.lower()
        adjustedKey = ""
        for i in range(len(text)):
            adjustedKey += self.key[i % len(self.key)]
        
        translation = ""
        for ch, k in zip(text, adjustedKey):
            if ch in self.characters:
                translation += self.translator_square[k][ch]
            else:
                translation += ch

        return translation


class RandomVigenere(Vigenere):
    def __init__(self, characters, key_length=7, seed=42):
        if seed is not None:
            random.seed(seed)
        key = ""
        for _ in range(key_length):
            key += random.choice(characters)

        Vigenere.__init__(self, characters=characters, key=key)


if __name__ == '__main__':
    vg = Vigenere('abcdefghijklmnopqrstuvwxyz', key='banana')

    s = vg.transform("Hello, Mom!")
    print(s)

    rvg = RandomVigenere('abcdefghijklmnopqrstuvwxyz', seed=42, key_length=7)

    s2 = rvg.transform("Hello, Mom!")
    print(s2)

