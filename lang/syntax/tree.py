from expression import *

class Tree(Expression):
  def __init__(self, args):
    self.expressions = args
  def evaluate(self, ev):
    out = []
    for e in self.expressions:
      out.append(ev.evaluate(e))
    return out
