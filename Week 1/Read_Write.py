CURREN_YEAR = 2021

print("Your firstname:")
firstname = input()

print("Your lastname:")
lastname = input()

print("Your name is " + firstname + " " + lastname )

print("When you were born:")
year_born = int(input())

age = CURREN_YEAR - year_born
print("You are " + str(age) + " year old in " + str(CURREN_YEAR))
