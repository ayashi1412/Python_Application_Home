#MODULE2.2.1.11 LAB Python Liberals

print('\"I\'m"\n\""learning""\n\"""Python"""')

#MODULE2.4.1.7 LAB Variables

John = 3
Mary = 5
Adam = 6
print(John , Mary , Adam, sep=",")

total_apples = John + Mary + Adam

print(total_apples)

#MODULE2.4.1.9 LAB Variables: A Simple Converter

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#MODULE2.4.10 LAB: Operators and expressions

x =  0
x = float(x)
y = (3 * x ** 3) - (2 * x ** 2) + (3 * x) - 1
print("y =", y)

#MODULE2.5.1.2 LAB: Comments

#this program computes the number of seconds in a given number of hours

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

#this is the end of the program that computes the number of seconds in 3 hour