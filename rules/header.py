class Rule:
  @classmethod
  def inc_header(cls, line, times):
    if len(line) == 0:
      return line
    elif line[0] == '-':
      return Rule.inc_header(line[1:], times + 1)
    else:
      if times > 0:
        css_class = 'jt-h' + str(times)
        return '<div class="%s">%s</div>' % (css_class, line.strip())
      else:
        return line

  @classmethod
  def match_header(cls, line):
    if len(line) < 2:
      return line
    elif line[0:2] == "#-":
      return Rule.inc_header(line[1:], 0)
    else:
      return line

  @classmethod
  def visit_line(cls, line):
    return Rule.match_header(line)

  @classmethod
  def visit(cls, text):
    return "\n".join([Rule.visit_line(line) for line in text.split("\n")])
