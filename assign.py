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
		self.size += 1

	def assign_numbers(self):
		for i in range(len(self.people)):
			self.people[i].number = i

	def dictToList(self, assignments):
		numbers = [0] * len(self.people)
		for i in range(len(self.people)):
			numbers[i] = assignments[i]
		return numbers

group = Group()
group.add_person("Sam", "sfarid93@gmail.com")
group.add_person("David", "david.w.aspinall@mgmail.com")
group.assign_numbers()




