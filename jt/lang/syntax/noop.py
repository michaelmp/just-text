from expression import *

class NoOp(Expression):
  def __init__(self):
    pass
  def evaluate(self, ev):
    return ''
