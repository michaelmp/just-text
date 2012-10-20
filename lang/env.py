class Environment:
  def __init__(self, parent, context):
    self.parent = parent
    self.env = {
      '__context__': context,
    }

  def bind(self, word, val):
    self.env[word] = val

  def lookup(self, word):
    if word in self.env.keys():
      answer = self.env[word]
      if type(answer) == type(lambda:0):
        return answer()
      elif type(answer) == str:
        return answer
      else:
        raise 'Unexpected construct!'
    else:
      if self.parent:
        return self.parent.lookup(word)
      else:
        return word
