
#Objective: Range Tasks

#Task 1: 
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(len(days_of_week)):     #Even index days
    if i % 2 == 0:
        print(days_of_week[i])

for i in range (len(days_of_week)):    #Odd index days
    if i % 2 != 0:
     print(days_of_week[i])
     
#2. Loop Condition Logic

#Task 1: 

flag = True

while flag:
    user = input("If you want to go to the movies tonight, then say Yes!")
    if user == "Yes!":
        flag = False


while True:
    i = input("Who makes the Dark Souls games?")
    if i == "From Software":
        print("Correct")
        break
    else:
        print("You have much to learn my young padawan, Answer again!")

    #Task 2:

count = 0 
while count <= 4:
    print("Iteration number ", count)
    count += 1
print(count)