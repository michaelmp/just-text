import re

from .. import error
from env import *
from syntax import *

ARGS = r'^([~_@*]*)$'
DEFINITION = r'^!([\w\-]+):( )*(.*)'
CALL = r'!([\w\-]+)( )*(.*)'

class Evaluator:
  def __init__(self, env = Environment(None, '')):
    self.env = env

  def push(self, context):
    self.env = Environment(self.env, context)

  def pop(self):
    if self.env.parent:
      self.env = self.env.parent

  def evaluate(self, expression):
    return expression.evaluate(self)

  # foo {a{b}c} bar {baz} => [foo {a{b}c} bar {baz}]
  def tokenize_line(self, line):
    out = []
    block = []
    nest = 0
    line = line.strip()
    grams = line.split(' ')
    for word in grams:
      nested = nest > 0
      if word[0] == '{':
        if nest == 0:
          word = word[1:]
        nest = nest + 1
        nested = True
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

    return words.Words(word)

  def scan_line(self, line):
    if len(line) == 0:
      return noop.NoOp()

    m = re.match(DEFINITION, line)
    if m:
      return definition.Definition(m.group(1), m.group(3))

    m = re.match(CALL, line)
    if m:
      return call.Call(m.group(1), m.group(3))

    return self.tokenize_line(line)

  def scan(self, context):
    return tree.Tree([self.scan_line(line) for line in context.splitlines()])
