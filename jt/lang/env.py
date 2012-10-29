import re
import sys

from .. import error

class Environment:
  def __init__(self, parent, context):
    self.parent = parent
    self.env = {
      '__context__': context,
    }

  def bind(self, word, val):
    if self.isbound(word) and not re.match(r'__\w+__', word):
      error.warning('"%s" is already defined.' % word)
    self.env[word] = val

  def isbound(self, word):
    if word in self.env.keys():
      return True
    elif self.parent:
      return self.parent.isbound(word)
    else:
      return False

  def lookup(self, word):
    if word in self.env.keys():
      answer = self.env[word]
      if type(answer) == type(lambda:0):
        return answer()
      elif type(answer) == str:
        return answer
      elif type(answer) == int:
        return answer
      else:
        raise 'Unexpected construct!'
    else:
      if self.parent:
        return self.parent.lookup(word)
      else:
        error.warning('"%s" is not defined.' % word)
        return word
