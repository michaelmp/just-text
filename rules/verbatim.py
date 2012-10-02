class Rule:
  @classmethod
  def visit_line(cls, line):
    line = line.replace('`'*3, '<span class="jt-pre">')
    line = line.replace('\''*3, '</span>')
    return line

  @classmethod
  def visit(cls, text):
    return '\n'.join([Rule.visit_line(line) for line in text.split('\n')])
