#appending by using python numpy
import numpy as np
a=np.array(input('enter a value of a'));
b=np.array(input('enter a value of b'));
print(a)
print(b)
l=len(a)
for k in range(0,1):
	b=np.append(b,a[k])
print b
