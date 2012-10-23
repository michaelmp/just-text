#!/usr/bin/env python

import sys

from jt.lang.eval import *

if __name__ == '__main__':
  sources = [
    ('lib/core.jt', open('lib/core.jt').read()),
    ('<stdin>', sys.stdin.read()),
  ]
  e = Evaluator()
  program = tree.Tree([
    e.scan_file(filename, source) for (filename, source) in sources
  ])
  error.okay('successfully parsed input')
  body = e.evaluate(program)
  error.okay('successfully compiled input')
  header = open('template/header.html').read()
  header = header.replace('%{title}', e.env.lookup('title'))
  css = '\n'.join([open(f).read() for f in [
    'css/jt.css',
    'css/screen.css',
    'css/print.css',
  ]])
  header = header.replace('%{css}', css)
  sys.stdout.write(header)
  sys.stdout.write(body)
  sys.stdout.write(open('template/footer.html').read())
  sys.stdout.flush()
  error.okay('all done')
