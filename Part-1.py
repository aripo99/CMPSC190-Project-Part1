import numpy as np
npz = np.load('part1a.npz')
lst = npz.files

for item in lst:
  print(item)
  print(npz[item])
