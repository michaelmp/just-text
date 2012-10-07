# TODO: Remove empty lines from output.

class Rule:
  @classmethod
  def visit_line(cls, line):
    if len(line.strip()) < 1:
      return ''
    elif line.strip()[0] == '#':
      return ''
    else:
      return line

  @classmethod
  def visit(cls, text):
    return '\n'.join([Rule.visit_line(line) for line in text.split('\n')])
