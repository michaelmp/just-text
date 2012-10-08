# TODO: Remove empty lines from output.
#
# "# This is a comment."


import re

pattern = r'# .*'

class Rule:

  @classmethod
  def visit_line(cls, line):
    if re.match(pattern, line):
      return ''
    else:
      return line

  @classmethod
  def visit(cls, text):
    return '\n'.join([Rule.visit_line(line) for line in text.split('\n')])
