userNumber = raw_input("Tell me a number. ")

try:
	userNumber = float(userNumber)
	#Only put lines that you expect to cause exceptions here
except ValueError:
	print("Umm, yeah, that's not a number...")
	exit()

finally:
	print("Double that is {}.".format(userNumber * 2)) 
