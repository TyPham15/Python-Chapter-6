#Class Exercise 1
def Project_1():
	def write_input():	#asks for user input and creates text file
		name = str(input('Enter your name: '))
		age = int(input('Enter your age: '))

		user_info = open('info.txt','w')

		user_info.write (name + '\n')
		user_info.write (f'Age: {age}')

		user_info.close()

		read_file()

	def read_file():	#reads the contents of the text file
		file_read = open('info.txt','r')
		contents = file_read.read()

		file_read.close()

		print(contents)

	write_input()
	return Project_1
#Project_1()


#Class Exercise 2
def Project_2():
	def WriteNumbers():	#user input and creating text file
		outfile = open('numbers.txt','a')

		num1 = int(input('enter #1 '))
		num2 = int(input('enter #2 '))
		num3 = int(input('enter #3 '))

		sum = num1 + num2 + num3
		avg = sum / 3

		outfile.write(f'the 1st number is {num1} \n')
		outfile.write(f'the 2nd number is {num2} \n')
		outfile.write(f'the 3rd number is {num3} \n')
		outfile.write(f'the average is {avg} \n')
		outfile.write(f'the total is {sum} \n')

		outfile.close()

		read_file()

	def read_file():	#reading the text file
		file = open('numbers.txt','r')
		contents = file.read()
		file.close()
		print(contents)

	WriteNumbers()
	return Project_2
#Project_2()


#Class Exercise 3
def Project_3():
	def sales_input():
		num_days = int(input('enter the days of sales: '))
		salary = int(input('enter the salary: '))
		total = 0
		sales_file = open('sales.txt','a')

		for count in range(1, num_days + 1):
			sales = float(input(f'enter the sales for day #{count}: '))
			sales_file.write(f'{sales} \n')
			total += sales

		if total > 1000:
			salary = (salary * 0.1) + salary

		sales_file.write(str(salary))
		sales_file.close()

		ReadSales()

	def ReadSales():
		sales_file = open('sales.txt','r')
		line = sales_file.readline()

		while line !='':
			amount = float(line)
			print(format(amount, '.2f'))
			line = sales_file.readline()

		sales_file.close()
	
	sales_input()
	return Project_3
#Project_3()


#Class Exercise 4
def Project_4():
