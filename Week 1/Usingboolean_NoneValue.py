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

if gender_input == "yes":
    is_male = True
elif gender_input == "no":
    is_male = False
else:
    is_male = None