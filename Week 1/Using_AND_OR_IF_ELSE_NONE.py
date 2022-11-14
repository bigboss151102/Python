CURRENT_YEAR = 2022
METTER_TO_FEET = 3.281

firstname = input("Your firstname: ")
lastname = input("Your lastname: ")
year_born = int(input("When you were born: "))
height_meter = float(input("You height (meter): "))

age = CURRENT_YEAR - year_born

height_feet = height_meter * METTER_TO_FEET
height_feet = round(height_feet, 1)

print("\n-----")
print("Your name is " + firstname + " " + lastname)
print("You is {0} year old in {1}".format(age, CURRENT_YEAR))
print("You are " + str(height_feet) + " feet tall")

gender_input = input("Are you male (yes/no): ")
is_male = None

if (gender_input == "yes") or (gender_input == "y") or (gender_input == "Yes"):
    is_male = True
elif (gender_input == "no") or (gender_input == "n") or (gender_input == "No"):
    is_male = False
else:
    is_male = None
    
if is_male == None:
    print("Invalid Answer")
elif is_male == True:
    if (height_feet > 6.5):
        print("You are very tall as a man")
    elif (height_feet > 6.0):
        print("You are tall as a man")
    else:
        print("You are sort as a man")
elif is_male == False:
    if(height_feet > 5.7):
        print("You are tall as a girl")
    else:
        print("You are sort as a girl")
else:
    print("System error:Variable 'is_male' is not correct")