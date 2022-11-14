from datetime import datetime


import datetime

def Ask_yes_no(prompt):
    answer = input(prompt)
    while True:
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            continue
        

def caculate_age(year_born):
    now = datetime.datetime.now()
    CURRENT_YEAR = now.year
    return CURRENT_YEAR - year_born


def convert_metter_to_feet(metter):
    METTER_TO_FEET = 3.281
    feet = metter * METTER_TO_FEET
    feet = round(feet,2)
    return feet
        
def print_height_info(height_feet, is_male):
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

def Print_Info(firstname, lastname, age, height_feet, is_VietNamese,is_male):
    now = datetime.datetime.now()
    CURRENT_YEAR = now.year
    print("\n-----")
    print("Your name is " + firstname + " " + lastname)
    print("You is {0} year old in {1}".format(age, CURRENT_YEAR))
    print("You are " + str(height_feet) + " feet tall")    
    if is_VietNamese == True:
        print("You are from Viet Nam")
    else:
        print("You are not from Viet Nam")
    print_height_info(height_feet, is_male)
    
def Ask_Person_info():
    firstname = input("Your firstname: ")
    lastname = input("Your lastname: ")
    year_born = int(input("When you were born: "))
    height_metter = float(input("You height(metter): "))
    return firstname, lastname, year_born, height_metter
            
def main():
    firstname, lastname, year_born, height_metter = Ask_Person_info()
    age = caculate_age(year_born)
    height_feet = convert_metter_to_feet(height_metter)
    is_male = Ask_yes_no("Are you male (yes/no):")
    is_VietNamese = Ask_yes_no("Are you from VietNamese (yes/no):")
    Print_Info(firstname, lastname, age, height_feet, is_VietNamese,is_male   )
        
main()