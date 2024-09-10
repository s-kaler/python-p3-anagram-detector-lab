# your code goes here!
class Anagram:

  def __init__(self, word):
    if isinstance(word, str):
      self.word = word
    else:
      print("word must be a string")
  
  def get_word():
    return self._word
  
  def set_word(self, word):
    self._word = word
  
  property(get_word, set_word)

  def match(self, wordList):
    matches = []
    for check_word in wordList:
      if sorted(check_word) == sorted(self.word):
        matches.append(check_word)
    return matches
