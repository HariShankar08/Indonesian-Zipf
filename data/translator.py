import random

class Translator:
    def __init__(self, characters, seed=42):
        self.characters = list(characters)
        
        random.seed(seed)
        self._translated_characters = list(characters)
        random.shuffle(self._translated_characters)
        
        self.dictionary = dict(zip(self.characters, self._translated_characters))
        self.inverse_dictionary = dict(zip(self._translated_characters, self.characters))

    def transform(self, text):
        txt = ''
        text = text.lower()
        for ch in text:
            if ch in self.dictionary:
                txt += self.dictionary[ch]
            else:
                txt += ch
        return txt
    
if __name__ == '__main__':
    tr = Translator('abcdefghijklmnopqrstuvwxyz ')
    print(tr.dictionary)