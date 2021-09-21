#SSgt Binod Gurung, Codes for Chapter 2.6.1.9 to 2.6.1.11.  Date: 21 Sept 2021

#MODULE 2.6.1.9 LAB: Simple Input and Output. Evaluating the results of 4 arithmetic operations.
 
a = float(input("Enter the first float value: ")) # input a float value for variable a here
b = float(input("Enter the second float value: "))# input a float value for variable b here

print("The sum of the float values is: " + str(a + b)) # output the result of addition here
print("The difference of the float values is: " + str(a - b)) # output the result of subtraction here
print("The product of the float values is: " + str(a * b)) # output the result of multiplication here
print("The Quotient of the float values is: " + str(a / b)) # output the result of division here
print("\nThat's all, folks!") #\n will start a newline after the print output.

#MODULE 2.6.1.10 LAB: Operators and expressions. Evaluate an algebric expression

x = float(input("Enter value for x: ")) #Input user's float value.
y = 1 / (x + (1/(x + (1/(x + (1/x)))))) # 1/x is represenation of 1/x in algrbric expression.
print("y =", y)

#MODULE 2.6.1.11 LAB: Operators and expressions. Evaluate the end time of a period of time.

hour = int(input("Starting time (hours): "))    #Input starting Time in hours.
mins = int(input("Starting time (minutes): "))  #Input starting Time in Minutes.
dura = int(input("Event duration (minutes): ")) #Input the event duration in Minutes.

Total_Minutes = (mins + dura)    #Calculates the total time spent in minutes.
End_Minutes = Total_Minutes % 60 #% 60 calculates the remainder of the minutes.
hr = hour + (Total_Minutes//60)  #//60 calculates the hour carried over.
End_hr = hr % 24                 #%24 calculates the 24 hr clock when the hr goes beyound 24.

print("The End time is ",End_hr,":",End_Minutes)
