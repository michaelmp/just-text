import sys

from expression import *

class Definition(Expression):
  def __init__(self, name, definition):
    self.name = name
    self.definition = definition

  def debug(self):
    sys.stderr.write('%s -> %s\n' % (self.name, self.definition))

  def evaluate(self, ev):
    value = lambda: ev.evaluate(ev.scan(self.definition))
    ev.env.bind(self.name, value)
    return ''
