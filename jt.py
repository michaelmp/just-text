#!/usr/bin/env python

import sys

from jt.lang.eval import *

if __name__ == '__main__':
  programs = [
    open('lib/core.jt').read(),
  ]
  programs.append(sys.stdin.read())
  error.okay('including core functions')
  source = '\n'.join(programs)
  e = Evaluator()
  scanned = e.scan(source)
  error.okay('successfully parsed input')
  body = e.evaluate(e.scan(source))
  error.okay('successfully compiled input')
  header = open('template/header.html').read()
  header = header.replace('%{title}', e.env.lookup('title'))
  header = header.replace('%{css}', open('css/jt.css').read())
  sys.stdout.write(header)
  sys.stdout.write(body)
  sys.stdout.write(open('template/footer.html').read())
  sys.stdout.flush()
  error.okay('all done')
