import re

from .. import error
from env import *
from syntax import *

ARGS = r'^([~_@*]*[@*]+[~_@*]*)$'
DEFINITION = r'^!([\w\-]+)( )*::( )*(.*)'
CALL = r'!([\w\-]+)( )*(.*)'
QUICK_CALL = r'!([\w\-]+)'
COMMENT = r'! .*'

class Evaluator:
  def __init__(self, env = Environment(None, '')):
    self.env = env

  def push(self, context):
    self.env = Environment(self.env, context)

  def pop(self):
    if self.env.parent:
      self.env = self.env.parent

  def evaluate(self, expression):
    try:
      return expression.evaluate(self)
    except Exception, e:
      filename = self.env.lookup('__filename__')
      line = self.env.lookup('__line__')
      error.fail('"%s" at %s:%s :: "%s"' % \
        (e, filename, line, expression))

  # foo {a{b}c} bar {baz} => [foo scan(a{b}c) bar scan(baz)]
  def tokenize_line(self, line):
    out = []
    block = []
    nest = 0
    line = line.strip()
    grams = line.split()
    for word in grams:
      nested = nest > 0
      if word[0] == '{':
        if nest == 0:
          word = word[1:]
        nest = nest + 1
        nested = True
      if len(word) > 0:
        if word[-1] == '}':
          nest = nest - 1
          if nest == 0:
            word = word[:-1]
          nested = True
        if nested:
          block.append(word)
        else:
          out.append(self.scan_word(word))
      if nest == 0:
        if len(block) > 0:
          out.append(self.scan(' '.join(block)))
          nest = 0
          block = []
    if nest != 0:
      error.fail('unbalanced {}')
    return sentence.Sentence(out)
  
  def scan_word(self, word):
    m = re.match(ARGS, word)
    if m:
      return args.Args(m.group(1))
    out = []
    for subword in re.split(QUICK_CALL, word):
      m = re.match(QUICK_CALL, subword)
      if m:
        out.append(call.Call(m.group(1), ''))
      else:
        out.append(words.Words(subword))
    return sentence.Sentence(out)

  def scan_line(self, line):
    if len(line) == 0:
      return noop.NoOp()
    m = re.match(COMMENT, line)
    if m:
      return words.Words('')
    m = re.match(DEFINITION, line)
    if m:
      return definition.Definition(m.group(1), m.group(4))
    m = re.match(CALL, line)
    if m:
      return call.Call(m.group(1), m.group(3))
    return self.tokenize_line(line)

  def scan(self, context):
    out = []
    for line in context.splitlines():
      self.env.bind('__line__', 1 + self.env.lookup('__line__'))
      scanned = self.scan_line(line)
      out.append(self.scan_line(line))
    return tree.Tree(out)

  def scan_file(self, filename, source):
    #try:
      error.info('Loading %s' % filename)
      self.env.bind('__filename__', filename)
      self.env.bind('__line__', 0)
      source = ' '.join(['{ '+line+' } {!atline}' for line in source.splitlines()])
      return self.scan(source)
    #except Exception, e:
    #  line = self.env.lookup('__line__')
    #  error.fail('"%s" at %s:%s :: "%s"' % \
    #    (e, filename, line, source.splitlines()[line - 1]))
