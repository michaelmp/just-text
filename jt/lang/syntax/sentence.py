import sys

from expression import *

class Sentence(Expression):
  def __init__(self, args):
    self.expressions = args
  
  def debug(self):
    sys.stderr.write(','.join([e.__class__.__name__ for e in self.expressions])+'\n')

  def evaluate(self, ev):
    return ' '.join([ev.evaluate(exp) for exp in self.expressions])
