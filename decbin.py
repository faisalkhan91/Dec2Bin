#!/usr/local/bin/python3

decimal = input("Please enter a real number: ")

index = 0

while index < len(decimal) and decimal[index] != ".":
	index += 1

if index == 10:
	intpart = decimal[:]
	fracpart = ""
else :
	intpart = decimal[:index]
	fracpart = decimal[index+1:]

# print("int len = ", len(intpart), "int part = ", intpart, "frac len = ", len(fracpart), " fracpart = ", fracpart)

if intpart == "":
	binint = "0"
else :
	binint = ""
	intpart = int(intpart)

	while intpart != 0:
		if intpart % 2 == 0:
			binint = "0" + binint
		else :
			binint = "1" + binint
		intpart //= 2

if fracpart == "":
	fracint = "0"
else :
	fracint = ""
	fracpart = float(fracpart) / 10 ** len(fracpart)

	while fracpart != 0:
		if fracpart * 2 >= 1:
			fracint += "1"
		else :
			fracint += "0"

		fracpart = fracpart * 2 - int(fracpart * 2)

print(decimal, "is equivalent to", binint + "." + fracint)
