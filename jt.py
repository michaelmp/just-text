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
  #verbatim.Rule,
  paragraph.Rule,
  header.Rule,
  remark.Rule,
]

def header(args = {}):
  template = TEMPLATE_HTML_HEADER
  template = template.replace('%{css}', CSS_INLINE + CSS_SCREEN + CSS_PRINT)
  template = template.replace('%{title}', args['title'])
  return template

def footer(args = {}):
  return TEMPLATE_HTML_FOOTER

def usage(args = {}):
  return 'USAGE: %s in.txt > out.html' % args['cmd']

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print(usage({'cmd': sys.argv[0]}))
  else:
    f = open(sys.argv[1], 'r')
    print(header({'title': sys.argv[1]}))
    formatted = f.read()
    for rule in RULES:
      formatted = rule.visit(formatted)
    print(formatted)
    print(footer())
