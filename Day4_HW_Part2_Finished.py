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

