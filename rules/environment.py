# "#:field: value" --> ENVIRONMENT[field] = value

import re

pattern = r'#:(\w+):(.*)'

class Rule:

  @classmethod
  def visit_line(cls, line):
    global ENVIRONMENT
    match = re.match(pattern, line)
    if match and match.group(1):
      print "%s -> %s" % match.group(1, 2)
      ENVIRONMENT[match.group(1)] = match.group(2)

  @classmethod
  def visit(cls, text):
    for line in text.split('\n'):
      Rule.visit_line(line)
    return text
