# Usage:
#
# !- Title
# !-- Part I
# !--- Chapter 1
# !---- ...

import re

pattern = r'^!([\-]+)(.*)'
element = '<div class="%s">%s</div>'
base_class = 'jt-h'

class Rule:
  @classmethod
  def visit_line(cls, line):
    match = re.match(pattern, line)
    if match:
      level = len(match.group(1))
      text = match.group(2)
      return element % (base_class+str(level), text)
    else:
      return line

  @classmethod
  def visit(cls, text):
    return '\n'.join([Rule.visit_line(line) for line in text.split('\n')])
