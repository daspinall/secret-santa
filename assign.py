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

group = Group()
group.add_person("Sam", "sfarid93@gmail.com")
group.add_person("David", "david.w.aspinall@mgmail.com")
group.assign_numbers()


#Returns a dictionary of numbers assigned to other numbers
def secret_santa(num_people):
	
	assignments = {}
	used_people = []

	while len(assignments.

	return assignments
