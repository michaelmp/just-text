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
  environment.Rule,
  remark.Rule,
]

ENVIRONMENT = {
  'title': 'Untitled',
  'author': 'Anonymous',
}

def header():
  template = TEMPLATE_HTML_HEADER
  template = template.replace('%{css}', CSS_INLINE + CSS_SCREEN + CSS_PRINT)
  template = template.replace('%{title}', ENVIRONMENT['title'])
  return template

def footer():
  return TEMPLATE_HTML_FOOTER

def usage(args = {}):
  return 'USAGE: %s in.txt > out.html' % args['cmd']

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print(usage({'cmd': sys.argv[0]}))
  else:
    ENVIRONMENT['title'] = sys.argv[1]

    f = open(sys.argv[1], 'r')
    formatted = f.read()
    for rule in RULES:
      formatted = rule.visit(formatted)

    print(header())
    print(formatted)
    print(footer())
