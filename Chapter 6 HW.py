#Project 1
#Number 1
def Challenge_1():
	def main():
		file = open('things.txt','a')
		file.write('Snake.\nApple.\nMexico.\n')
		file.close()
	main()
#Challenge_1()


#Number 2
def Challenge_2():
	def main():
		file = open('things.txt','r')
		content = file.read()	#reading the file
		file.close()
		print(content)	#print out saved contents of the file
	main()
#Challenge_2()


#Number 3
def Challenge_3():
	def main():
		file = open('number_lists.txt','w')
		n = 0
		for count in range(100):	#for loop to write out the numbers to 100
			n += 1
			file.write(str(n) + '\n')
		file.close()
	main()
#Challenge_3()


#Project 2
#Number 5
def Challenge_5():
	import tkinter as tk
	
	win = tk.Tk()	#first window for the user to click yes or no
	win.geometry('300x50')
	win.title('Contents of Text File')

	ask_prompt = tk.Label(win, text = "Do you want to read the contents of the file?").grid(column = 0, row = 0)

	def write():	#makes and writes out the contents of the "numbers" file, including the total of the numbers
		n = 0
		total = 0
		text_file = open('numbers.txt','w')
		for count in range(10):
			n += 100
			text_file.write(f'{n}\n')
			total += n
		text_file.write(f'The total is {total}.')
		text_file.close()

	def new_window():	#generates a new window after the user clicks on yes to display all the contents of the file
		win2 = tk.Toplevel()
		win2.geometry('100x200')
		win2.title('Inside the Text File')
		file = open('numbers.txt','r')
		content = file.read()
		file.close()
		showfile = tk.Label(win2, text = content).grid(column = 0, row = 0)

	def quit():	#quit function, for whenever the user clicks on no
		win.destroy()

	btnYes = tk.Button(win, text = "Yes", command = new_window).grid(column = 0, row = 2)

	btnNo = tk.Button(win, text = "No", command = quit).grid(column = 1, row = 2)

	write()
	win.mainloop()
#Challenge_5()