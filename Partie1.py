import random

class RandomSentence:
    # constructor with all the sentences available
    def __init__(self):
        self._sentences = [
            "Un grand pouvoir implique de grande responsabilité",
            "Tes frites sur place ou a emportrer",
            "6 mac nuggets et une grand frite",
            "c'est pas l'homme qui prend la mere, c'est la mere qui prend l'homme",
            "la vie est dure, mais pas autant que pithon"
        ]

    # getter
    def get_sentences(self):
        return self._sentences
    
    # setter
    def set_sentences(self, sentences):
        self._sentences = sentences;

    # return a random sentence in the sentences list 
    def getRandom(self):
        return self._sentences[random.randint(0, len(self._sentences) - 1)];

rs = RandomSentence();
print(rs.getRandom())