from expression import *

class Words(Expression):
  def __init__(self, context):
    self.context = context
  def evaluate(self, ev):
    return self.context
