import re

first_p = True
regex_skip = r'[\#].*'

class Rule:
  @classmethod
  def visit(cls, text):
    strbuilder = []
    for par in text.split('\n\n'):
      if len(par.strip()) > 0:
        if re.match(regex_skip, par.strip()):
          first_p = True
          strbuilder.append(par)
        else:
          strbuilder.append('<div class="jt-p">%s</div>' % par.strip())
          first_p = False
    return '\n'.join(strbuilder)
