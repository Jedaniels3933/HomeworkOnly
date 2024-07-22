

food = ['pizza' , 'burger', 'fries', 'apple','fries', 'cake','cake', 'Key_pie' ]

for i in range (len(food)):
    print(i, food[i])
    if food[i] == 'cake':
        print("Cake position:", i)


students = ['John', 'Jim', 'Jane', 'Jill']
grades = [98, 84, 76, 100]
act = ['FB', 'soccer', 'BB', 'tennis']

for i in range(len(students)):
    print(students[i], "has a grade of", grades[i], "and plays", act[i])

grouped_info = zip(students, grades, act)
print(grouped_info)

for i in zip(students, grades, act):
    print(i[0], "has a grade of", i[1], "and plays", i[2])

    









