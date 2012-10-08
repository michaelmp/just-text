#!/usr/bin/env python

import sys

from rules import *

TEMPLATE_HTML_HEADER = open('template/header.html', 'r').read()
TEMPLATE_HTML_FOOTER = open('template/footer.html', 'r').read()
CSS_INLINE = open('css/jt.css', 'r').read()
CSS_SCREEN = open('css/screen.css', 'r').read()
CSS_PRINT = open('css/print.css', 'r').read()

# Order matters.
RULES = [
  paragraph.Rule,
  header.Rule,
  environment.Rule,
  remark.Rule,
  substitute.Rule,
]

def header():
  env = environment.VARIABLES
  template = TEMPLATE_HTML_HEADER
  template = template.replace('%{css}', CSS_INLINE + CSS_SCREEN + CSS_PRINT)
  template = template.replace('%{title}', '%s, by %s' % (env['title'], env['author']))
  return template

def footer():
  return TEMPLATE_HTML_FOOTER

def usage(args = {}):
  return 'USAGE: %s < in.txt > out.html' % args['cmd']

if __name__ == '__main__':
    formatted = sys.stdin.read()
    if len(formatted) < 1:
      print(usage({'cmd': sys.argv[0]}))
    else:
      for rule in RULES:
        formatted = rule.visit(formatted)
      print(header())
      print(formatted)
      print(footer())
