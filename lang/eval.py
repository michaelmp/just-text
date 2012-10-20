import re

from env import *
from syntax import *

ARGS = r'^([~_@*]*)$'
BLOCK_CALL = r'(.*){(.*)}(.*)' #TODO: balance workaround
DEFINITION = r'^!([\w\-]+):( )*(.*)'
CALL = r'!([\w\-]+)( )*(.*)'

DEBUG = True

def depth(env, level):
  if env.parent:
    return depth(env.parent, level + 1)
  else:
    return level

class Evaluator:
  def __init__(self, env = Environment(None, '')):
    self.env = env

  def push(self, context):
    self.env = Environment(self.env, context)

  def pop(self):
    if self.env.parent:
      self.env = self.env.parent

  def evaluate(self, expression):
    if DEBUG:
      print('--'*depth(self.env, 1) + expression.__class__.__name__)
    return expression.evaluate(self)

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

    m = re.match(BLOCK_CALL, line)
    if m:
      return sentence.Sentence([
        self.scan(m.group(1)),
        self.scan(m.group(2)),
        self.scan(m.group(3)),
      ])

    return sentence.Sentence([self.scan_word(word) for word in line.split()])

  def scan(self, context):
    return tree.Tree([self.scan_line(line) for line in context.splitlines()])
