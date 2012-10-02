class Rule:
  @classmethod
  def visit(cls, text):
    strbuilder = []
    for par in text.split('\n\n'):
      if len(par.strip()) > 0:
        strbuilder.append('<div class="jt-p">%s</div>' % par.strip())
    return '\n'.join(strbuilder)
