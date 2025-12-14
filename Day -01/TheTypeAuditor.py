'''Goal: Ask the user to type a number.
1 . Print the type() of the raw input.
2.	Cast it to a float.
3.	Print the type() again.'''

number = input("Enter a number: ")

print("Type of the raw input is: ",type(number))

number_in_float = float(number)

print("Type of the input number after casting is: ",type(number_in_float))
