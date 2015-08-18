# TODO create unique random list of 8 numbers with only one cycle

from random import randint

class Group:

	class Person:
		def __init__(self, name, email):
			self.number = -1
			self.name = name
			self.email = email

	def __init__(self):
		self.people = []

	def add_person(self, name, email):
		self.people.append(self.Person(name, email))

	def assign_numbers(self):
		for i in range(len(self.people)):
			self.people[i].number = i

	#Returns a dictionary of numbers assigned to other numbers
	def secret_santa(self):
		
		assignments = {}
		current = 0
		assignment = randint(1, len(self.people) - 1)

		for person in range(len(self.people) - 1):

			assignments[current] = assignment
			current = assignment
			if len(assignments.keys()) == len(self.people) - 1:
				break
			
			assignments[current] = -1

			while assignments.has_key(assignment):
				assignment = randint(0, len(self.people) - 1)

		assignments[current] = 0

		return assignments

	def dictToList(self, assignments):
		numbers = [0] * len(self.people)
		for i in range(len(self.people)):
			numbers[i] = assignments[i]
		return numbers

group = Group()
group.add_person("Sam", "sfarid93@gmail.com")
group.add_person("David", "david.w.aspinall@mgmail.com")
group.assign_numbers()


