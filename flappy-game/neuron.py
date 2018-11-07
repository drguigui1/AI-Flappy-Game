"""
Copyright :
 - Cesar Belley
 - Pierre Guillaume
"""

from random import gauss

class Neuron():
	"""
	Representation of a neuron
	Gaussian rapartition for bias and weight
	"""

	def __init__(self, nb_inputs):
		self.weights = []
		for i in range(nb_inputs):
			self.weights.append(gauss(0, 0.3))
		self.bias = gauss(0, 0.3)


 		