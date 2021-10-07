class Person:
	def __init__(self, name, age, height, parents=[], siblings=[]):
		self.name = name
		self.age = age
		self.height = height
		self.parents = parents
		self.siblings = siblings

	def __str__(self):
		response = self.name
		for sibling in self.siblings:
			response += f'\n- {sibling.name}'
		return response

	def add_sibling(self, sibling):
		self.siblings.append(sibling)

	def add_parent(self, parent):
		self.parents.append(parent)

	def num_siblings(self):
		return len(self.siblings)

	def total_heights(self):
		total = 0
		for sibling in siblings:
			total += sibling.height
		return total
