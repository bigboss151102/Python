user_input = int(input("Enter an interger:"))

with open("data.txt","w") as file:
    for i in range(user_input):
        file.write(str(user_input - i)+ "\n")
        
number = []

with open("data.txt" , "r") as file:
    number = file.read().split("\n")
    number.pop()
    
for i in range(len(number)):
    print("Line " + str(i+1) + ":" + number[i] )
