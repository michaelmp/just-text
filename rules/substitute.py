# For an environment variable defined "#:title:The Title",
# "The name of this text is {title}" substitutes "The Title".

import re

import environment

pattern = r'\{(\w+)\}'

class Rule:

  @classmethod
  def env_lookup(cls, match):
    env = environment.VARIABLES
    if match.group(1) in env.keys():
      return env[match.group(1)]
    else:
      return ''

  @classmethod
  def visit_line(cls, line):
    return re.sub(pattern, Rule.env_lookup, line)

  @classmethod
  def visit(cls, text):
    return '\n'.join([Rule.visit_line(line) for line in text.split('\n')])
