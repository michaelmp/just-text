#!/usr/bin/env python

import sys

from lang.eval import *

if __name__ == '__main__':
  programs = [
      open('lib/core.jt').read(),
  ]
  programs.append(sys.stdin.read())
  source = '\n'.join(programs)
  e = Evaluator()
  body = e.evaluate(e.scan(source))
  header = open('template/header.html').read()
  header = header.replace('%{title}', e.env.lookup('title'))
  header = header.replace('%{css}', open('css/jt.css').read())
  print(header)
  print(body)
  print(open('template/footer.html').read())
