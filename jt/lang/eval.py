import re

from .. import error
from env import *
from syntax import *

ANY_COMMAND = r'^( )*!.*$'

ONE_LINE_DEF = r'^( )*![\w-]+:.*[\S].*$'
MULTI_LINE_DEF = r'^( )*![\w-]+:( )*$'
ONE_LINE_CALL = r'^( )*![\w-]+ .*[\S].*$'
MULTI_LINE_CALL = r'^( )*![\w-]+( )*$'

DEFINITION = r'!([\w-]+):( )*(.*)'
CALL = r'!([\w-]+)( )+(.*)'

ARGS = r'^([~_@*]*[@*]+[~_@*]*)$'

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

  def tokenize(self, line):
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
          out.append(self.parse_word(word))
      if nest == 0:
        if len(block) > 0:
          out.append(self.parse_command(' '.join(block)))
          nest = 0
          block = []
    if nest != 0:
      error.fail('unbalanced {}')
    return sentence.Sentence(out)
  
  def parse_word(self, word):
    m = re.match(ARGS, word)
    if m:
      return args.Args(m.group(1))
    return words.Words(word)

  def parse_command(self, line):
    if len(line) == 0:
      return noop.NoOp()
    #m = re.match(COMMENT, line)
    #if m:
    #  return words.Words('')
    m = re.match(DEFINITION, line)
    if m:
      return definition.Definition(m.group(1), m.group(3))
    m = re.match(CALL, line)
    if m:
      return call.Call(m.group(1), m.group(3))
    return self.tokenize(line)

  def bracketize(self, source):
    indent_stack = [0]
    multi_stack = []
    grams = []
    for line in source.splitlines():
      whitespace = len(line) - len(line.lstrip())
      if whitespace > indent_stack[-1]:
        grams.append('{')
        indent_stack.append(whitespace)
      else:
        if re.match(ANY_COMMAND, line):
          while len(multi_stack) > 0:
            grams.append(multi_stack.pop())
          while whitespace < indent_stack[-1]:
            indent_stack.pop()
            grams.append('}')
      if re.match(ONE_LINE_DEF, line) or re.match(ONE_LINE_CALL, line):
        grams.append('{')
        grams.extend(line.split())
        grams.append('}')
      elif re.match(MULTI_LINE_DEF, line) or re.match(MULTI_LINE_CALL, line):
        grams.append('{')
        grams.extend(line.split())
        multi_stack.append('}')
      else:
        grams.extend(line.split())
    while len(multi_stack) > 0:
      grams.append(multi_stack.pop())
    while len(indent_stack) > 1:
      indent_stack.pop()
      grams.append('}')
    return ' '.join(grams)

  def scan(self, jtstr):
    b = self.bracketize(jtstr)
    return self.tokenize(b)
