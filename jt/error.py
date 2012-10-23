import sys

color_red = '\033[0;31;m'
color_green = '\033[0;32;m'
color_yellow = '\033[0;33;m'
color_blue = '\033[0;34;m'
color_end = '\033[0;;m'

def warning(msg):
  sys.stderr.write('[%swarn%s] %s\n' % (color_yellow, color_end, msg))
  sys.stderr.flush()

def fail(msg):
  sys.stderr.write('[%sfail%s] %s\n' % (color_red, color_end, msg))
  sys.stderr.flush()
  sys.exit()

def okay(msg):
  sys.stderr.write('[ %sok%s ] %s\n' % (color_green, color_end, msg))

def info(msg):
  sys.stderr.write('[%sinfo%s] %s\n' % (color_blue, color_end, msg))

