#TASK 1

usernumber = int(input("Enter a number: "))
usernumber_list = []

for i in range(usernumber):
    usernumber = input("number_list: ")
    usernumber_list.append(usernumber_list)

#TASK 2
usernumber = (input("Do you want clear the list or not? : (yes or no?)"))
if usernumber == "yes":
    usernumber_list.clear()
elif usernumber == "no":
    userdata = int(input("enter new data: "))
    usernumber_list.append(userdata)

print(usernumber_list)

#TASK 3
username = ["MARGA","MARGARETTE","MIKO"]
userdata = input("Do you want to remove an element by index or by name?: ")
if username == "by index":
    userdata.pop()
elif username == "by name":
    userdata.remove(username)

print(username)

#task 4

number_list = [1,2,3,4]
name_list =  ["MARGA","CUTE KO", "CUTIE"]

number_list = input("Do you want to sort or reverse this?: ")
name_list = input("Do you want to sort or reverse this?: ")

if number_list == "by sort":
    number_list.sort(number_list)
elif number_list == "by reverse":
    number_list.reverse(number_list)

print(number_list)

if name_list == "by sort":
    name_list.sort(name_list)
elif name_list == "by reverse":
  name_list.reverse(name_list)

print(name_list)
   


