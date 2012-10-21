import sys

color_red = '\033[0;31;m'
color_green = '\033[0;32;m'
color_yellow = '\033[0;33;m'
color_end = '\033[0;;m'

def warning(msg):
  sys.stderr.write('[%s warning %s] %s\n' % (color_yellow, color_end, msg))
  sys.stderr.flush()

def error(msg):
  sys.stderr.write('[%s  error  %s] %s\n' % (color_red, color_end, msg))
  sys.stderr.flush()

def okay(msg):
  sys.stderr.write('[%s  okay   %s] %s\n' % (color_green, color_end, msg))
