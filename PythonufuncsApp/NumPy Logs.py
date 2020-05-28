# NumPy Logs By ChisoftMedia
from math import log

import numpy as np

# Log at Base 2

arr = np.arange(1, 10)
print(np.log2(arr))


# Log at Base 10
arr = np.arange(1, 10)

print(np.log10(arr))

# Natural Log, or Log at Base e
arr = np.arange(1, 10)

print(np.log(arr))

# Log at Any Base
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
