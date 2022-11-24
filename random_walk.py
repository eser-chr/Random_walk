import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# A class for n-dim random walk. Does not save path.
# Time O(N)
# Memory O(1)

class RandomWalk:
	def __init__(self, N = 1000, dim = 2):
		self.N = N
		self.dim = dim
		self.position = self.initial()

	def initial(self):
		return np.zeros(self.dim)

	def run(self):
		x = np.random.randint(2*self.dim, size = self.N)
		return x

	def decode(self):
		for i in self.run():
			self.position[i//2] += 2 * (i%2 - 0.5)

s = RandomWalk(N = 100000, dim = 2)
s.run()
print(s.position)
s.decode()
print(s.position)