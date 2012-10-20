from env import *
from syntax import *

class Evaluator:
  def __init__(self, env = Environment(None)):
    self.env = env

  def evaluate(self, expression):
    return expression.evaluate(self)

  def scan_line(self, line):
    if len(line) == 0:
      return noop.NoOp()
    return words.Words(line)

  def scan(self, context):
    ast = []
    for line in context.splitlines():
      ast.append(self.scan_line(line))
    return tree.Tree(ast)
