#name  = input("Enter your Name: ")
#age  = int(input("Enter your age: "))
#
#print(f"Hello {name}, your are {age} years old.")

#a = int(input("Enter value of first number: "))
#b = int(input("Enter value of second number: "))
#
#sum = a + b
#diff = a - b
#prod = a * b
#quotient = a / b
#
#print(sum)
#print(diff)
#print(prod)
#print(quotient)

#temperature = float(input("Enter the temperature in Celsius: "))
#
#Fahrenheit = (temperature*1.8) + 32
#
#print("Temperature in Fahrenheit: ", Fahrenheit)

#a = 10
#b = 20
#print(f"Before Swapping a is {a} and b is {b}")
#
#c = b
#b = a
#a = c
#print(f"After Swapping a is {a} and b is {b} ")

#a = 10
#b = 20
#
#print(f"before swapping a is {a} and b is {b}")
#
#a = a+b
#b = a-b
#a = a-b
#
#print(f"after swapping a is {a} and b is {b}")

#number = int(input("Enter a number: "))
#
#if number > 0:
#    print("The number is positive")
#elif number < 0:
#    print("The number is negative")
#else :
#    print("The number is zero")

#Word = str(input("Enter a string: "))
#
#print(len(Word))
#print(Word[0])
#print(Word[-1])

#
#    num  = int(input("Enter a number: "))
#
#if num % 3 == 0 and num % 5 == 0:
#    print("The number is divisible by both 3 and 5")
#elif num % 3  == 0 and num % 5 != 0:
#    print("The number is only divisible by 3 not 5")
#elif num % 3 != 0 and  num % 5 == 0:
#    print("The number is only divisible by 5 not 3")
#else:
#    print("Number is not divisible by either 3 or 5")
#

#text = input("Enter a string: ")
#
#vowels = "aeiouAEIOU"
#
#if any(x in vowels for x in text):
#    print("Yes")
#else:
#    print("No")

#text = str(input("Enter the string: "))
#
#upper_count = 0
#lower_count = 0
#
#for x in text:
#    if x.isupper():
#        upper_count += 1
#    elif x.islower():
#        lower_count +=1
#
#print("Uppercase Letters: ", upper_count)
#print("Lowercase Letters: ", lower_count)

#text  = str(input("Enter a string: "))
#print(text.replace(" ",""))
#OR
#text = str(input("Enter a string: "))
#print("".join(text.split()))
    

#text = input("Enter a string: ")

#rev = ""
#for ch in text:
#    rev = ch + rev

#print("Reversed:", rev)

#OR

#text  = str(input("Enter the string: "))
#
#rev = ""
#i = len(text) - 1

#while i>=0:
#    rev += text[i]
#    i -= 1

#print("Reversed String: ", rev)

text = input("Enter a string: ")
#normalize
text = text.replace(" ","").lower()

rev = ""
for ch in text:
    rev = ch + rev

print("Reversed:", rev)

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")








    



 


