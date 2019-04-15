class first(object):
	def _init_(self):
		self.s = ""
	def getstring(self):
		self.s = input("Enter string:")
	def printstring(self):
		print(self.s.upper())
obj1 = first()
obj1.getstring()
obj1.printstring()
