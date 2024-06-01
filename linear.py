#list = [1,30,50,45,90,87,78]
total = int(input("how many numbers?"))
list=[]
for i in range(total):
    x = int(input("enter your number"))
    list.append(x)
    
num = int(input("Please enter the number:"))

if num in list:
    index = 0
    for i in list:
        if i == num:
            print("number found at ", index," index")
        index = index +1
else:
    print("Not present in the list")


#Time Complexity of the above Algorithm is O(n).