## this program will convert US dollars to Euros. Programmed by Benji Wheelock

#ask the user i they want to use the program and save to a variable
answer = input("Would you like to use the program? (y/n) ")

while answer == "y":

    dollar = int(input("Enter your dollor amount "))
    euro = dollar * .94540
    print("your euro amount is " + str(euro))
    answer = input("Would you like to use the program? (y/n) ")


