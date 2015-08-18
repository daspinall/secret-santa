# TODO create unique random list of 8 numbers with only one cycle

from random import randint

class Group:

	class Person:
		def __init__(self, name, email):
			self.number = -1
			self.name = name
			self.email = email

	def __init__(self):
		self.size = 0
		self.people = []

	def add_person(self, name, email):
		self.people.append(self.Person(name, email))
		self.size += 1

	def assign_numbers(self):
		for i in range(self.size):
			self.people[i].number = i

	#Returns a dictionary of numbers assigned to other numbers
	def secret_santa(self, num_people):
		
		assignments = {}
		current = 0
		assignment = randint(1, num_people - 1)

		while len(assignments.keys()) < num_people:

			assignments[current] = assignment

			current = assignment

			while assignments.has_key(assignment):
				assignment = randint(0, num_people - 1)

		return assignments


group = Group()
group.add_person("Sam", "sfarid93@gmail.com")
group.add_person("David", "david.w.aspinall@mgmail.com")
group.assign_numbers()


