import turtle
abel = turtle.Turtle()
num = int(input('Enter a number: '))
dog = 2*int(num)
print('The number you entered multiplied by two is ' +str(dog)+ '.')
if (dog % 2) == 0:
    print("{0} is even".format(dog))
else:
    print("{0} is odd".format(dog))

for i in range(4):
    abel.forward(num)
    abel.right(90)
