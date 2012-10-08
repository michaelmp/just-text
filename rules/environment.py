# "#:field: value" --> ENVIRONMENT[field] = value

import re

pattern = r'#:(\w+):(.*)'

VARIABLES = {
  'title': 'Untitled',
  'author': 'Anonymous',
}

class Rule:

  @classmethod
  def visit_line(cls, line):
    global VARIABLES
    match = re.match(pattern, line)
    if match and match.group(1):
      VARIABLES[match.group(1)] = match.group(2)
      return ''
    else:
      return line

  @classmethod
  def visit(cls, text):
    return '\n'.join([Rule.visit_line(line) for line in text.split('\n')])
