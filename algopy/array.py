class Array:
	# variables
	__array = [];
	__length = 0;
	# functions
	
	# constructor
	def __init__(self,length):
		self.__length = length
		self.__array = [None] * length

	# __getitem__ operator
	def __getitem__(self,key):
		if key < 0 or key >= self.__length:
			raise NameError('Index out of bound')
		return self.__array[key]

	# __setitem__ operator
	def __setitem__(self,key,item):
		if key < 0 or key >= self.__length:
			raise NameError('Index out of bound')
		self.__array[key] = item

	# Get the size of the array
	def length(self):
		return self.__length

	# Print array
	def print(self):
		for i in range(self.__length):
			print(str(self.__array[i])+" ",end="")
		print()

a = Array(10)
for i in range(10):
	a[i] = i

a.print()

