#!/usr/bin/env python

import os
import sys

from jt.lang.eval import *
from jt import error
from jt.lang import debug

if __name__ == '__main__':
  try:
    ROOT_DIR = os.environ['JT_ROOT']
  except:
    raise Exception("Oh no! Couldn't find JT_ROOT in environment. :(")

  sources = [
    (ROOT_DIR+'/lib/core.jt', open(ROOT_DIR+'/lib/core.jt').read()),
    (ROOT_DIR+'/lib/resume/resume.jt', open(ROOT_DIR+'/lib/resume/resume.jt').read()),
    ('<stdin>', sys.stdin.read()),
  ]
  e = Evaluator()
  program = source.Source([
    e.scan(source) for (filename, source) in sources
  ])
  error.okay('successfully parsed input')
  body = e.evaluate(program)
  error.okay('successfully compiled input')
  header = open(ROOT_DIR+'/template/header.html').read()
  header = header.replace('%{title}', e.env.lookup('--title--'))
  css = '\n'.join([open(f).read() for f in [
    ROOT_DIR+'/css/jt.css',
    ROOT_DIR+'/css/screen.css',
    ROOT_DIR+'/css/print.css',
    ROOT_DIR+'/lib/resume/resume.css',
  ]])
  header = header.replace('%{css}', css)
  sys.stdout.write(header)
  sys.stdout.write(body)
  sys.stdout.write(open(ROOT_DIR+'/template/footer.html').read())
  sys.stdout.flush()
  error.okay('all done')
