from expression import *

class Sentence(Expression):
  def __init__(self, args):
    self.expressions = args
  def evaluate(self, ev):
    #TODO: discriminate whitespace conditions
    return ' '.join([ev.evaluate(exp) for exp in self.expressions])
