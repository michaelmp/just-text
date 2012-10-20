# Usage:
#
# !field: value
#
# {field} => value
#
# Also,
#
# !function: @@
#
# {function These are the arguments.}
# => These are the arguments.

import re

import environment
from function import Function

pattern = r'\{(\w+)(.*)\}'

class Rule:

  #TODO: proper lang, with environments, parse/evaluate
  # {f1 {f2 the whole enchilada}}

  @classmethod
  def evaluate(cls, string):
    out = []
    for word in string.split():
      out += eval_word(word)
    return ' '.join(out)

  @classmethod
  def env_lookup(cls, match):
    env = environment.VARIABLES
    key = match.group(1)
    args = match.group(2)
    if key in env.keys():
      if type(key) == Function:
        return key.apply(args)
      elif type(key) == str:
        return env[key]
      else:
        return ''
    else:
      return ''

  @classmethod
  def visit_line(cls, line):
    return re.sub(pattern, Rule.env_lookup, line)

  @classmethod
  def visit(cls, text):
    return '\n'.join([Rule.visit_line(line) for line in text.split('\n')])
