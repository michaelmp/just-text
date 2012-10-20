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
  print(e.evaluate(e.scan(source)))
