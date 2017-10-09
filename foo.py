print __name__
if (__name__ == '__main__'):
   print 'running file directly'
if (__name__ == "foo"):
   print "running foo.py as module"


import Kylesmodule

Kylesmodule.py
==============

class KylesClass:

   def __init__():
      print 'constructing class'

   def doSomething(self):
      ...

   def doSomethingElse(self)
      ...

from Kylesmodule import KylesClass
kyleobj = KyleClass()
kyleobj.doSomething()
kyleobj.doSomethingElse()
