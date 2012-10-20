class Environment:
  def __init__(self, parent):
    self.parent = parent
    self.env = {}

  def bind(self, word, val):
    self.env[word] = val

  def lookup(self, word, context):
    if word in self.env.keys():
      if type(word) == type(lambda:0):
        return word()
      elif type(word) == str:
        return self.env[word]
      else:
        raise 'Unexpected construct!'
    else:
      if self.parent:
        return self.parent.lookup(word)
      else:
        return word
