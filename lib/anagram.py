# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        new_anagram = []
        for word in word_list:
            if sorted(word) == sorted(self.word):
                new_anagram.append(word)
        return new_anagram


listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana', 'silent'])
print(result)