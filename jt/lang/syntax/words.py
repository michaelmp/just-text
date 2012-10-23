import sys

from expression import *

class Words(Expression):
  def __init__(self, context):
    self.context = context

  def debug(self):
    sys.stderr.write('%s\n' % self.context)

  def evaluate(self, ev):
    return self.context
