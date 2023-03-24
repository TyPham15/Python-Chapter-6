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
		outfile = open('number.txt','a')

		num1 = int(input('enter #1 '))
		num2 = int(input('enter #2 '))
		num3 = int(input('enter #3 '))

		sum = num1 + num2 + num3
		avg = sum / 3

		#writes the variables into the file
		outfile.write(f'the 1st number is {num1} \n')
		outfile.write(f'the 2nd number is {num2} \n')
		outfile.write(f'the 3rd number is {num3} \n')
		outfile.write(f'the average is {avg} \n')
		outfile.write(f'the total is {sum} \n')

		outfile.close()

		read_file()

	def read_file():	#reading the text file
		file = open('number.txt','r')
		contents = file.read()
		file.close()
		print(contents)

	WriteNumbers()
	return Project_2
#Project_2()


#Class Exercise 3
def Project_3():
	def sales_input():	#all user input
		num_days = int(input('enter the days of sales: '))
		salary = int(input('enter the salary: '))
		total = 0
		sales_file = open('sales.txt','a')

		for count in range(1, num_days + 1):	#for loop to enter the sales of a specific day in order
			sales = float(input(f'enter the sales for day #{count}: '))
			sales_file.write(f'{sales} \n')
			total += sales

		if total > 1000:
			salary = (salary * 0.1) + salary

		sales_file.write(str(salary))
		sales_file.close()

		ReadSales()

	def ReadSales():	#read the contents of file
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
	def main():
		num_emps = int(input('enter the number of employee records'))
		emp_file = open ('employees.txt', 'w')
		
		for count in range(1, num_emps +1):
			print('enter data for employee #', count)

			name = input("Name: ")
			id_num = input ("ID NUMBER: ")
			dept = input('DEPARTMENT: ')

			emp_file.write(name +'\n')
			emp_file.write(id_num +'\n')
			emp_file.write(dept +'\n')

			print()

		emp_file.close()
		print('recorded')

		file = open('employees.txt','r')	#reading the contents of file
		contents = file.read()
		file.close()
		print(contents)

	main()
	return Project_4
#Project_4()


#Class Exercise 5
def Project_5():
	import tkinter as tk
	from tkinter import messagebox

	win = tk.Tk()
	win.geometry("300x100")
	win.title("Customer Information")

	lblLastname = tk.Label(win, text = "enter the last name").grid(column = 0, row = 0)
	lblFirstname = tk.Label(win, text = "enter the first name").grid(column = 0, row = 1)

	#extra information shown in the window
	lblAddress = tk.Label(win, text = "enter the address").grid(column = 0, row = 2)
	lblCity = tk.Label(win, text = "enter the city").grid(column = 0, row = 3)
	lblState = tk.Label(win, text = "enter the state").grid(column = 0, row = 4)
	lblZipcode = tk.Label(win,text = "enter the zip code").grid(column = 0, row = 5)


	def write():
		text_file = open("Customers.txt", "a")
		content = text_file.write("\nConfirmation: " + str(LN.get()) + ", " + str(FN.get()) + ", " + str(AD.get()) + ", " + str(CI.get()) + ", " + str(ST.get()) + ", " + str(ZC.get()))
		text_file.close()
		messagebox.showinfo("information","Data Recorded")

	def quit():
		messagebox.showinfo("information","Thank you...")
		win.destroy()

	def submit():
		messagebox.showinfo("information","entered :" + LN.get() + "," + FN.get() + "," + AD.get() + "," + CI.get() + "," + ST.get() + "," + ZC.get())

	LN = tk.StringVar()
	txtLastname = tk.Entry(win, width = 12, textvariable = LN).grid(column = 1, row = 0)
	FN = tk.StringVar()
	txtFirstname = tk.Entry(win,width = 12, textvariable = FN).grid(column = 1, row = 1)

	#extra information to ask from the user
	AD = tk.StringVar()
	txtAddress = tk.Entry(win, width = 12, textvariable = AD).grid(column = 1, row = 2)
	CI = tk.StringVar()
	txtCity = tk.Entry(win, width = 12, textvariable = CI).grid(column = 1, row = 3)
	ST = tk.StringVar()
	txtSTate = tk.Entry(win, width = 12, textvariable = ST).grid(column = 1, row = 4)
	ZC = tk.StringVar()
	txtZipCode = tk.Entry(win, width = 12, textvariable = ZC).grid(column = 1, row = 5)



	btnSubmit = tk.Button(win, text = "submit", command = submit).grid(column = 0, row = 8)

	btnQuit = tk.Button(win, text = "quit", command = quit).grid(column = 1, row = 8)

	btnWrite = tk.Button(win, text = "transfer", command = write).grid(column = 2, row = 8)

	win.mainloop()
	submit()
#Project_5()


#Class Exercise 6
def Project_6():
	import tkinter as tk
	from tkinter import messagebox

	win = tk.Tk()
	win.geometry = ('250x250')

	#shown on the window as text
	number1 = tk.Label(win, text = 'enter the first number').grid(column = 0, row = 0)
	number2 = tk.Label(win, text = 'enter the second number').grid(column = 0, row = 1)
	number3 = tk.Label(win, text = 'enter the third number').grid(column = 0, row = 2)

	def write():	#writes to the file
		file = open('sum.txt','a')
		content = file.write("\nYou entered the numbers: " + str(N1.get()) + ", " + str(N2.get()) +  ", " +str(N3.get()) + "\n")

		sum = N1.get() + N2.get() + N3.get()
		avg = sum / 3

		content = file.write(f'The sum is {sum}.\n')
		content = file.write(f'The average is {avg}.\n')

		messagebox.showinfo('Data', 'Data has been recorded.')
		win.destroy()

	#user input boxes on the window
	N1 = tk.IntVar()
	txtNumber1 = tk.Entry(win, width = 12, textvariable = N1).grid(column = 1, row = 0)
	N2 = tk.IntVar()
	txtNumber2 = tk.Entry(win, width = 12, textvariable = N2).grid(column = 1, row = 1)
	N3 = tk.IntVar()
	txtNumber3 = tk.Entry(win, width = 12, textvariable = N3).grid(column = 1, row = 2)

	btnSubmit = tk.Button(win, text = "submit", command = write).grid(column = 0, row = 4)

	win.mainloop()
#Project_6()


#Class Exercise 7
def Project_7():
	def main():	#user input while also opening and writing to the file
		name = str(input('Enter the full name of the student: '))
		midterm = float(input('Enter the grade of the midterm: '))
		final = float(input('Enter the grade of the final exam: '))

		avg = (midterm + final) / 2

		file = open('grades.txt','a')
		file.write('Student Name: ' + str(name) + '\n')
		file.write('Midterm Grade: ' + str(midterm) + '\n')
		file.write('Final Exam Grade: ' + str(final) + '\n')

		#try and catch statement to test validity of user input
		if True:
			try:
				if avg <= 100 and avg >= 90:
					file.write('The average grade is an A. ' + str(avg) + '\n')

				elif avg <= 89 and avg >= 80:
					file.write('The average grade is an B. ' + str(avg) + '\n')

				elif avg <= 79 and avg >= 70:
					file.write('The average grade is an C. ' + str(avg) + '\n')

				elif avg <= 69 and avg >= 60:
					file.write('The average grade is an D. ' + str(avg) + '\n')

				elif avg < 60:
					file.write('The average grade is an F. ' + str(avg) + '\n')

				file.close()

				read_file = open('grades.txt','r')
				content = read_file.read()
				read_file.close()
				print(content)

			except ValueError:
				print('Error in the values of the grades.')
			except Exception as err:
				print(err)

	main()
#Project_7()


#Class Exercise 8
def Project_8():
	def main():

		import random
		open_file = open('random.txt','w')	#opens file and asks for how many numbers the user wants to choose
		amount = int(input('This program will choose random numbers from 1 to 10. How many numbers do you want to choose: '))

		for count in range(amount):	#for loop to choose the specific amount of numbers chosen by the user
			n = random.randint(1, 10)
			open_file.write(str(n) + '\n')

		open_file.close()

		#reading the contents of the file
		file = open('random.txt','r')
		content = file.read()
		file.close()
		print(content)

	main()
#Project_8()