colors = ["Red" , "Green" , "Blue" , "Yellow"]

print(colors)

#remove from list 
try:
    colors.remove("Green")
except:
    print("Not Exist")

### Chú ý câu lệnh trong Try sẽ thực hiện trước nếu nó không sai thì
### nó sẽ thực hiện và bỏ qua câu lệnh Except, nếu sai thì câu lệnh 
### except được thực hiện

print(colors)

# remove last elemet
colors.pop()
print(colors)

colors.insert(0,"Black")
print(colors)

colors.insert(1,"Purple")
print(colors)

### In ra vi tri
colors = ["Red" , "Green" , "Blue" , "Yellow" , "Red"]
try:
    print("The first index of 'Red", end="")
    print(colors.index("Red"))
except:
    print("Not Exist")
    
# find index of "Red" in list
red_index = []
for i in range(len(colors)):
    if colors[i] == "Red":
        print("The index element 'Red' in List:", end="")
        print(red_index.append[i])
    else:
        print("Not exist")
    
#find number of occurance of "Red"
print("How many time 'Red' occurs: "+ str(colors.count("Red")))

#Sort Example:
print("Sort Example:")
a = [1,2,10,4,5,0,6]
a.sort()
print(a)

#Change the first element 
a[0] = "100"
print(a)


