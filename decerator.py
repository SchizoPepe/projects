#whenever you're creating a decorator function, the first function takes the function, the 2nd function is the one that's called
def func(f):  #'f' parameter takes a function
	def wrapper():
		print("Started")
		f()  #calls whichever function that was passed in
		print("Ended\n")
	return wrapper  #we have to return wrapper because it's inside of 'func'

def func2():
	print("This is func2")
def func3():
	print("This is func3")

x = func(func2)  #'x' stores whatever we return in 'func'. We pass func2 as the parameter for func
x()  #we call the function 'func'
y = func(func3)
y()

func2 = func(func2)  #simply doing this allows us to type func2() to call 'func'
func2()
