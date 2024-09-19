# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab6A.py
def isValid(width, height):
    print("This is a valid rectangle." if (width+height)>=30 else "This is an invalid rectangle.")
    valid = True if (width+height)>=30 else False
    return valid
def area(width, height, valid):
    if valid:
        print(f"The area is: {width * height}")
def perimiter(width, height, valid):
    if valid:
        print(f"The perimeter is: {(2*width) + (2*height)}")
run = True
while run:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    valid = isValid(width, height)
    area(width, height, valid)
    perimiter(width, height, valid)
    run = True if input("Do you want to enter another width and height (Y/N)?: ").lower() == "y" else False
print("Program Ends")