#if condition
i = 10
if(i % 2):
    print "Odd Number"
else:
    print "Even Number"
    
print '\n'

#Defining a function of even numbers    
def isEven(numbers):
    return number % 2 == 0
isEven(3)

def evens(numbers):
	acc = 0
	for i in (numbers):
		if (i % 2 == 0):
			acc = acc + i
	return acc

print evens([1, 6, 3, 7, 5, 8])
print evens([76, 9, 43, 7])
			

