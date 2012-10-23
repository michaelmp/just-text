import sys

from .. import debug
from .. import env
from expression import *

class Call(Expression):
  def __init__(self, name, context):
    self.name = name
    self.context = context

  def debug(self):
    sys.stderr.write('%s ( %s )\n' % (self.name, self.context))

  def evaluate(self, ev):
    if debug.DEBUG:
      print(' ' * debug.depth(ev.env, 0) + \
          "!'%s' -> %s" % (self.name, self.context))
    ev.push(ev.evaluate(ev.scan(self.context)))
    out = ev.env.lookup(self.name)
    ev.pop()
    return out
