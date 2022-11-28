class people:
	firstname=''
	lastname=''
	age=0
	def __init__(self, firstname, lastname, age):
		self.firstname = firstname
		self.lastname=lastname
		self.age = age

p1 = people('Bill','Appiah', 25)
p2 = people('Steve','Mensah', 29)
p3 = people('Ravi','Donkor', 26)

people_list = [p1, p2, p3]
# student_list.sort() # raise an error

people_list.sort(key=lambda s: s.lastname) # sorts using lambda function
people_list.sort(key=lambda a: a.age)
people_list.sort(key=lambda f: f.firstname)

print('Students in Ascending Order:\n', end=' ')

for std in people_list:
	print(std.firstname, end=', ')
print('\n')

people_list.sort(key=lambda s: s.firstname, reverse=True) # sorts using lambda function

print('Students in Descending Order:\n', end=' ')

for std in people_list:
	print(std.lastname, end=', ')
print('\n')
print("list the ages of the students\n")

for std in people_list:
	print(std.age, end=', ')	
	