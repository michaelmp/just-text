import sys

from expression import *

class Tree(Expression):
  def __init__(self, args = []):
    self.expressions = args

  def evaluate(self, ev):
    return '\n'.join([ev.evaluate(exp) for exp in self.expressions])
