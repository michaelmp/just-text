# Destructures arguments based on ascii-art regex!!!
#
# @ => (word)
# _@ => word (word)
# __@ => word word (word)

import re
import sys

from expression import *

def destructure(symbol):
  if symbol == '@':
    return '([\S]+)'
  if symbol == '_':
    return '[\S]+'
  if symbol == '~':
    return '.*'
  if symbol == '*':
    return '(.*)'
  return ''

class Args(Expression):
  def __init__(self, pattern):
    pattern = ' '.join([destructure(s) for s in pattern])
    self.pattern = re.compile('^' + pattern + '$')

  def debug(self):
    sys.stderr.write('%s\n' % self.pattern)

  def evaluate(self, ev):
    try:
      return ' '.join(re.findall(self.pattern, ev.env.lookup('__context__')))
    except: # Do nothing when ambiguous results.
      return ''
