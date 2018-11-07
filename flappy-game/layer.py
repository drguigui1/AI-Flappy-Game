"""
Copyright :
 - Cesar Belley
 - Pierre Guillaume
"""

from neuron import Neuron

class Layer():
	"""
	A layer is composed by some neurons
	"""

	def __init__(self, nb_inputs, nb_neurons):
		self.neurons = []
		for i in range(nb_neurons):
			self.neurons.append(Neuron(nb_inputs))
 	
	def __str__(self):
		chaine = "----------\n"
		for i in range(len(self.neurons)):
			chaine += "neuron n°" + str(i + 1) + ":\n"
			chaine += "--> weights: " + str(self.neurons[i].weights) + "\n"
			chaine += "--> bias: " + str(self.neurons[i].bias) + '\n'
		chaine += "----------"
		return chaine