def farmSize(a, b):
  big = max(a, b)
  small = min(a, b)
  if big % small == 0:
    return small
  else:
    return farmSize(big - small, small)

