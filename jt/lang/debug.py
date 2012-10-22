DEBUG = True 

def depth(env, level):
  if env.parent:
    return depth(env.parent, level + 1)
  else:
    return level
