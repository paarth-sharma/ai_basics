import unittest

class stack: #Using a list as a stack
	def __init__(self):
		self.p = []
		
	def push(self,t):
		if(self.pushable(t)):
			self.p.append(t)
			return True
		else:
			return False
			
	def pop(self):
		return self.p.pop()
		
	def top(self):
		if self.p:
			return self.p[-1]
		
	def remove(self):
		self.p.pop(0)
		
	def isEmpty(self):
		return (len(self.p)==0)
		
	def printStack(self):
		print(self.p)
		
	def isFull(self):
		return (len(self.p) >= 3)
		
	def pushable(self,t):
		if (self.isFull()):
			return False
		else:
			return self.isEmpty() or t < self.top()
			
	def size(self):
		return len(self.p)
	def equal(self, s):
		return self.p == s.p
		
class stackTests(unittest.TestCase):
	def setUp(self):
		self.s = stack()
	
	def test_pushable(self):
		#Check that 1 is pushable to an empty stack
		self.assertTrue(self.s.pushable(1))
		
		#Check that 1 is not pushable to a stack with 1 on it
		self.s.push(1)
		self.assertTrue(not self.s.pushable(1))
		
		#test pop while we are at it
		self.assertTrue(self.s.pop() == 1)
		
		#test with full stack
		for x in range(3,0,-1):
			self.s.push(x)
		self.assertFalse(self.s.push(0))

	def test_equal(self):
		comp = stack()
		self.assertTrue(not self.s.equal(comp))
		
		comp.push(3)
		self.s.push(3)
		self.assertTrue(self.s.equal(comp))
		
		self.s.push(2)
		self.s.push(1)
		comp.push(2)
		comp.push(1)
		self.assertTrue(self.s.equal(comp))