# wanna make passowrd guesser for example a can put in only 4 numbers but im allowed to type from 0-9
# count combinations of 4 with possible numbers of 10
# is it possible?

amount = int(input("[+] How many numbers 4 combi9tions? "))

numbers = []
clone_numbers = []
var = 0


def looper():
	for i in range(amount):
		numbers.append(i)
		clone_numbers.append(i)

def reaper():

	for new_lst in numbers:
		print( new_lst,end=' ')

	print(end='\n')


def counter():
	while True:
		try:
			for i in range(len(numbers)):
				var = numbers[i]
				numbers[i] = numbers[i+1]
				numbers[i+1] = var
				reaper()

		except:
			if numbers == clone_numbers:
				break

			else:
				pass



looper()
counter()
print('\n' + "*-" * 25 + '\n')

print(f"Unique Amount of combinations are - {int(len(numbers))**2-int(len(numbers))}")
print(f"initial number list is {clone_numbers}")

print('\n' + "*-" * 25 + '\n')
