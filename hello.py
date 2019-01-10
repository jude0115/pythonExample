# Simple print
print('Hello Python')

# input
name = input('Please write your name')
print 'Hello, ' + name

# for loop
print 'for loop' 
for i in range(0,10):
	print i

#while loop
print 'while loop'
x = 0
while x < 10:
	x+=1
	print x

#function
def add(var1, var2):
	return var1 + var2

print 'function'
var1 = input('Please type first number')
var2 = input('Please type second number')
result = add(var1, var2)
print 'result = '  
print result
