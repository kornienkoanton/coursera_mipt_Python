import sys
import math
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
#print ((-b+math.sqrt(b**2-4*a*c))/2*a)
#print ((-b-math.sqrt(b**2-4*a*c))/2*a)
print (int((-b+math.sqrt(b**2-4*a*c))/2*a if (b**2-4*a*c) >= 0 else print ("rehenia net")))
print (int((-b-math.sqrt(b**2-4*a*c))/2*a if (b**2-4*a*c) > 0 else print ("rehenia net")))