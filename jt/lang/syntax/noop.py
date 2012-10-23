from expression import *

class NoOp(Expression):
  def __init__(self):
    pass

  def debug(self):
    return ''

  def evaluate(self, ev):
    return ''
