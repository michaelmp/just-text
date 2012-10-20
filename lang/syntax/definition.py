from expression import *

class Definition(Expression):
  def __init__(self, name, context):
    self.name = name
    self.context = context
  def evaluate(self, ev):
    value = lambda: ev.evaluate(ev.scan(self.context))
    evaluator.env.bind(self.name, value)
    return ''
