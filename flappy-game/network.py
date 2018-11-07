"""
Copyright :
 - Cesar Belley
 - Pierre Guillaume
"""

from layer import Layer
from functions import sigmoid

class Network():
	"""
	size : [1, 6, 1] 
	-> 1 neurone for the firstlayer, 6 for second one...
	"""

	def __init__(self, size):
		self.num_layer = len(size)
		self.nb_inputs = size[0]
		self.nb_ouputs = size[-1]
		self.layers = []
		for i in range(1, self.num_layer):
			self.layers.append(Layer(size[i-1], size[i]))
		"""
		for i in self.layers:
			print(i)
		"""
	
	def feed_forward(self, input_array):
		value_layers = []
		value_layers.append(input_array)
		
		for i in range(self.num_layer - 1):
			tab = []
			for j in range(len(self.layers[i].neurons)):
				nb = 0				
				for k in range(len(self.layers[i].neurons[j].weights)):
					nb += self.layers[i].neurons[j].weights[k] * value_layers[i][k]		
				nb += self.layers[i].neurons[j].bias
				tab.append(sigmoid(nb))
			value_layers.append(tab)
		return value_layers[-1]


