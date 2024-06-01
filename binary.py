#list = [1,30,50,45,90,87,78]
total = int(input("how many numbers?"))
list=[]
for i in range(total):
    x = int(input("enter your number"))
    list.append(x)
list.sort()  
print(list) 
num = int(input("Please enter the number:"))

search = False
start = 0
end = len(list) - 1

while start <= end:
    mid = (start+end)// 2 #floor division #returns a whole number quotient
    if list[mid] == num:
        print("Found at", mid, "index")
        search = True
        break
    elif list[mid] > num:
        end = mid - 1 
    else:
        start = mid + 1
if search == False:
    print("value not found")
