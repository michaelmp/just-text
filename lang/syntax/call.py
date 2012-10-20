from expression import *

class Call(Expression):
  def __init__(self, name, context):
    self.name = name
    self.context = context
  def evaluate(self, ev):
    return ev.env.lookup(self.name, ev.scan(self.context))
