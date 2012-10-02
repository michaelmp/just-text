class Rule:
  @classmethod
  def visit_line(cls, line):
    if len(line.strip()) < 2:
      return line
    elif line.strip()[0:2] == '--':
      return ''
    else:
      return line

  @classmethod
  def visit(cls, text):
    return '\n'.join([Rule.visit_line(line) for line in text.split('\n')])
