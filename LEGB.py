'''
LEGB --> Local Enclosing, Golbal, Buu=ilt-in

import builtins
#print(dir(builtins))

x= 'global x'

def test():
	global x
	x = 'local x'
	print(x)	

#test()

def min(*args):
	pass
m = min([3,6,2,6,68,7])
'''

x = 'out side Global x'

def outer():
	x = 'outer x'

	def inner():
		nonlocal  x
		x = 'Inner x'
		print(x)

	inner()
	print(x)
outer()
print(x)

