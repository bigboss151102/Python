# write mode - write to a new file
with open("data.txt", "w") as file:
    file.write("Hoang Cong Trong\n")
    file.write("Love\n")
    file.write("Nguyen Ha Giang")
    
with open("data.txt","w") as file:
    file.write("a\n")
    file.write("b\n")
    
# Append mode - write to an existing file
with open("data.txt","a") as file:
    file.write("c\n")
    file.write("d\n")
    file.write("e")
    
with open("data.txt","r") as file:
    data = file.read()
    print(data)                 