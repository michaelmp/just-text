#!/usr/bin/env python

import sys

from rules import *

TEMPLATE_HTML_HEADER = open('template/header.html', 'r').read()
TEMPLATE_HTML_FOOTER = open('template/footer.html', 'r').read()
CSS_INLINE = open('jt.css', 'r').read()

# Order matters.
RULES = [
  remark.Rule,
  header.Rule,
  verbatim.Rule,
  paragraph.Rule,
]

def header(args = {}):
  template = TEMPLATE_HTML_HEADER
  template = template.replace('%{css}', CSS_INLINE)
  template = template.replace('%{title}', args['title'])
  return template

def footer(args = {}):
  return TEMPLATE_HTML_FOOTER

def usage():
  return 'USAGE: ./jt.py file.txt > file.html'

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print(usage())
  else:
    f = open(sys.argv[1], 'r')
    print(header({'title': sys.argv[1]}))
    formatted = f.read()
    for rule in RULES:
      formatted = rule.visit(formatted)
    print(formatted)
    print(footer())
